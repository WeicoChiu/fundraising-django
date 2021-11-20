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
    # path('', views.index, name='index'),
    path('<int:id>/', views.project_detail, name='project_detail'),
    path('show/', views.show_project, name='show_project'),
    path('create/', views.create_project, name='create_project'),
    path('search/', views.search, name='search'),
    path('caregory/<int:id>/', views.show_category, name='show_category'),
    path('update/<int:id>/', views.update_project, name='update_project'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
    path('create-projectsupport/<int:id>', views.create_projectsupport, name='create_projectsupport'),
]
