import json
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from project.models import Pledge, ProjectSupport, Project

from . import newebpayform
from .models import Payment


# Create your views here.
@login_required(redirect_field_name=None)
def order(request):
    quantity = int(request.POST['quantity'])
    project_support_id = int(request.POST['project_support_id'])
    curr_support = ProjectSupport.objects.get(id=project_support_id)
    curr_project = curr_support.project
    total = int(curr_support.price) * quantity

    merchant_order_no = 'EX' + datetime.now().strftime('%s')

    pledge = Pledge.objects.create(
        user = request.user,
        projectsupport = curr_support,
        projectName = curr_project.title,
        price = total,
        supportname= curr_support.name,
        supportprice= curr_support.price,
        quantity=quantity,
        merchant_order_no = merchant_order_no
    )

    form_info = newebpayform.form_to_newebpay(merchant_order_no, total, curr_project.title)

    context = {
        'merchantid': form_info['merchantid'],
        'tradeinfo': form_info['tradeinfo'],
        'tradesha': form_info['tradesha'],
        'version': form_info['version']
    }
    return  render(request, 'payment/submit.html', context)

@login_required(redirect_field_name=None)
def list(request):
    pledges = Pledge.objects.filter(user=request.user)
    context = {'pledges': pledges}
    return render(request, 'payment/payment_list.html', context)


@csrf_exempt
def trade_finish(request):
    if request.POST['Status'] == 'SUCCESS':
        trade_info = request.POST['TradeInfo']
        trade_sha = request.POST['TradeSha']
        if newebpayform.check_trade_sha(trade_info, trade_sha):
            trade_info = newebpayform.decrypt_unpad(trade_info)
            trade_info_json = json.loads(trade_info)
            result = trade_info_json['Result']
            if result['PaymentType'] == 'CREDIT':
                pledge = Pledge.objects.get(merchant_order_no=result['MerchantOrderNo'])
                context = {'pledge': pledge}
                return render(request, 'payment/credit_payment.html', context)
    return HttpResponse('Payment Failure')

@csrf_exempt
def notify(request):
    if request.POST['Status'] == 'SUCCESS':
        trade_info = request.POST['TradeInfo']
        trade_sha = request.POST['TradeSha']
        if newebpayform.check_trade_sha(trade_info, trade_sha):
            trade_info = newebpayform.decrypt_unpad(trade_info)
            trade_info_json = json.loads(trade_info)
            result = trade_info_json['Result']
            pledge = Pledge.objects.get(merchant_order_no=result['MerchantOrderNo'])
            pledge.status = 'paid'
            pledge.save()
            if result['PaymentType'] == 'CREDIT':
                Payment.objects.create(
                    pledge=pledge,
                    merchant_order_no=result['MerchantOrderNo'],
                    total=result['Amt'],
                    status=request.POST['Status'],
                    paid_date=result['PayTime']
                )
            elif result['PaymentType'] == 'VACC':
                pledge.status = 'paid'
                pledge.save()
                payment = Payment.objects.get(pledge=pledge)
                payment.paid_date = result['PayTime']
                payment.save()
            project = Project.objects.get(title=pledge.projectName)
            project.total_donate += result['Amt']
            project.count_donate += 1
            project.save()
            return HttpResponse('payment executing')
    else:
        if newebpayform.check_trade_sha(trade_info, trade_sha):
            trade_info = newebpayform.decrypt_unpad(trade_info)
            trade_info_json = json.loads(trade_info)
            result = trade_info_json['Result']
            pledge = Pledge.objects.get(merchant_order_no=result['MerchantOrderNo'])
            pledge.status = 'expired'
            return HttpResponse('payment error')
    return HttpResponse('payment failure')

@csrf_exempt
def atm(request):
    if request.POST['Status'] == 'SUCCESS':
        trade_info = request.POST['TradeInfo']
        trade_sha = request.POST['TradeSha']
        if newebpayform.check_trade_sha(trade_info, trade_sha):
            trade_info = newebpayform.decrypt_unpad(trade_info)
            trade_info_json = json.loads(trade_info)
            result = trade_info_json['Result']
            pledge = Pledge.objects.get(merchant_order_no=result['MerchantOrderNo'])
            pledge.status = 'unpaid'
            pledge.save()
            Payment.objects.create(
                pledge=pledge,
                merchant_order_no=result['MerchantOrderNo'],
                total=result['Amt'],
                status=request.POST['Status'],
                expired_date=result['ExpireDate'] + " " + result['ExpireTime'],
                bank_code=result['BankCode'],
                code_no=result['CodeNo']
            )
            context = {'pledge': pledge}
            return render(request, 'payment/atm_payment.html', context)
    return HttpResponse('Access failure')

def status(request, id):
    pledge = Pledge.objects.get(id=id)
    context = {'pledge': pledge}
    if pledge.status == 'unpaid':
        return render(request, 'payment/atm_payment.html', context)
    else:
        return render(request, 'payment/credit_payment.html', context)
