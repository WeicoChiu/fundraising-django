from django import forms
from .models import Project, ProjectSupport

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 'category','description',
            'goal', 'image',
        ]
        labels = {
            'title': '專案名稱',
            'category': '類別',
            'description': '專案描述',
            'goal': '目標金額',
            'image': '圖片',
        }

    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
        # add form-control to each form
        for name, field in self.fields.items():
          field.widget.attrs.update({'class': 'form-control'})

class DonatePlanForm(forms.ModelForm):
    class Meta:
        model = ProjectSupport
        fields = [
            'name', 'description',
            'price',
        ]
        labels = {
            'name': '贊助方案',
            'description': '贊助描述',
            'price': '價格',
        }

    def __init__(self, *args, **kwargs):
        super(DonatePlanForm, self).__init__(*args, **kwargs)
        # add form-control to each form
        for name, field in self.fields.items():
          field.widget.attrs.update({'class': 'form-control'})