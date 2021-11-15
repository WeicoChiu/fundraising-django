from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def create(request):
    return HttpResponse('Hello World!!!')

def member_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, '信箱或密碼輸入不正確')

    return render(request, 'member/login.html')

def member_logout(request):
    logout(request)
    return redirect('index')