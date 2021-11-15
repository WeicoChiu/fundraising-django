from django.forms import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreation, self).__init__(*args, **kwargs)
        # change label name
        self.fields['username'].label = "使用者名稱"
        self.fields['email'].label = "信箱"
        self.fields['password1'].label = "密碼"
        self.fields['password2'].label = "確認密碼"
        # add form-control to each form
        for name, field in self.fields.items():
          field.widget.attrs.update({'class': 'form-control'})
