from django.shortcuts import redirect, render
from project.models import Pleadge, ProjectSupport
from . import newebpayform
from datetime import datetime

# Create your views here.
def order(request):
    quantity = int(request.POST['quantity'])
    project_support_id = int(request.POST['project_support_id'])
    curr_support = ProjectSupport.objects.get(id=project_support_id)
    curr_project = curr_support.project
    total = int(curr_support.price) * quantity

    pleadge = Pleadge.objects.create(
        user = request.user,
        projectsupport = curr_support,
        projectName = curr_project.title,
        price = total,
        supportname= curr_support.name,
        supportprice= curr_support.price,
        quantity=quantity
    )

    merchant_order_no = 'EX' + datetime.now().strftime('%s')

    form_info = newebpayform.form_to_newebpay(merchant_order_no, total, curr_project.title)

    print(form_info)
    context = {
        'merchantid': form_info['merchantid'],
        'tradeinfo': form_info['tradeinfo'],
        'tradesha': form_info['tradesha'],
        'version': form_info['version']
    }
    return  render(request, 'payment/submit.html', context)