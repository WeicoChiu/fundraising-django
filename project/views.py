from urllib import request

from django.http import HttpResponse
from django.shortcuts import render

from .models import Category, Pleadge, Project, ProjectOwner
from django.contrib.auth.decorators import login_required
from .form import ProjectCreationForm, DonatePlanForm
from django.shortcuts import redirect

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
            return redirect('show_project')

    print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'project/create_project.html', context)
