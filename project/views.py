from builtins import object
from urllib import request

from astroid.protocols import instance_class_infer_binary_op
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from .form import DonatePlanForm, ProjectCreationForm
from .models import Category, Pleadge, Project, ProjectOwner, ProjectSupport


# Create your views here.
def index(request):
    projects = Project.objects.filter(status='published')
    context = {'projects': projects}
    return render(request, 'base.html', context)

def search(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        projects = Project.objects.filter(Q(status='published') &
                                          Q(title__icontains=search) |
                                          Q(description__icontains=search)
                                        ).distinct()
        context = {'projects': projects, 'search': search}
        return render(request, 'project/search.html', context)
    else:
      return redirect('index')

def show_category(request, id):
    category = Category.objects.get(id=id)
    projects = category.projects.all()
    context = {'projects': projects}
    return render(request, 'project/show_category.html', context)

def project_detail(request, id):
    project = Project.objects.get(id=id)
    projectsupport = project.projectsupport

    context = {'project': project, 'projectsupport': projectsupport}
    return render(request, 'project/project_detail.html', context)

@login_required(redirect_field_name=None)
def show_project(request):
    try:
        projectowner = ProjectOwner.objects.get(user_id=request.user.id)
    except ProjectOwner.DoesNotExist:
        projectowner = ProjectOwner.objects.create(user= request.user)
    projects = projectowner.projects.all()
    categories = Category.objects.all()

    context = {'projects': projects}
    return render(request, 'project/show_project.html', context)

@login_required(redirect_field_name=None)
def create_project(request):
    form = ProjectCreationForm()

    if request.method == 'POST':
        form = ProjectCreationForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            projectowner = ProjectOwner.objects.get(user_id=request.user.id)
            project.projectowner = projectowner
            project.save()
            return redirect('create_projectsupport', id=project.id)

    context = {
        'form': form,
    }
    return render(request, 'project/create_project.html', context)

@login_required(redirect_field_name=None)
def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectCreationForm(instance=project)

    if request.method == 'POST':
        form = ProjectCreationForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project.save()
            return redirect('show_project')

    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'project/update_project.html', context)

@login_required(redirect_field_name=None)
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()

    return redirect('show_project')


@login_required(redirect_field_name=None)
def create_projectsupport(request, id):
    form = DonatePlanForm()
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = DonatePlanForm(request.POST)
        if form.is_valid():
            projectsupport = form.save(commit=False)
            projectsupport.project = project
            projectsupport.save()
            project.status = 'published'
            project.save()
            return redirect('index')

    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'project/create_projectsupport.html', context)

