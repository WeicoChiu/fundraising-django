"""fundrasing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('order/', views.order, name='order'),
    path('list/', views.list, name='payment_list'),
    path('notify/', views.notify, name='payment_notify'),
    path('atm/', views.atm, name='payment_atm'),
    path('status/<int:id>/', views.status, name='status'),
    path('trading-finish/', views.trade_finish, name='trading-finish'),
]
