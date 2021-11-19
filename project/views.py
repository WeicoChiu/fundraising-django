from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Pleadge, Project, ProjectOwner
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'base.html', context)

def project_detail(request, id):
    project = Project.objects.get(id=id)
    projectsupport = project.projectsupport

    context = {'project': project, 'projectsupport': projectsupport}
    return render(request, 'project/project_detail.html', context)

@login_required(redirect_field_name=None)
def create_project(request):
    projectowner = ProjectOwner.objects.get(user_id=request.user.id)
    projects = projectowner.projects.all()
    categories = Category.objects.all()

    context = {'projects': projects}
    return render(request, 'project/create_project.html', context)