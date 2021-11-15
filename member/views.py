from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import CustomUserCreation


# Create your views here.
def member_register(request):
    form = CustomUserCreation()
    if request.method == "POST":
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()

            # mutiple autentication you should choose one
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')

    context = {'form': form}
    return render(request, 'member/register.html', context)

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