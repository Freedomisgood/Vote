#_*_ utf-8 _*_
from django import forms
from . import models
class LoginForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=10)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())