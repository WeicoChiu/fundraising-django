from django.contrib import admin

from .models import Category, Pleadge, Project, ProjectOwner, ProjectSupport


# Register your models here.
@admin.register(ProjectOwner)
class ProjectOwnerAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectowner', 'category', 'title', 'description', 'goal')
    exclude = ('total_donate', 'count_donate')

@admin.register(ProjectSupport)
class ProjectSupportAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'description', 'price')

@admin.register(Pleadge)
class PleadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'projectsupport', 'projectName', 'price', 'issuedate', 'status', 'supportname', 'supportprice', 'quantity')
