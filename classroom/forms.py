from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,User
from  django import forms
from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2','is_student','is_teacher']