__author__ = 'Marcus Stockton'
from django import forms
from .models import User
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget
from django.forms import ModelForm, extras


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    cv = forms.FileField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            'birth_date',
            'first_name',
            'last_name',
            'email',
            "avatar",
            "cv"
        )


class UserForm(ModelForm):
    avatar = forms.ImageField(required=False)
    cv = forms.FileField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "birth_date",
            "avatar",
            "cv"
        ]
        widgets = {
            "birth_date": extras.SelectDateWidget(years=range(1900, datetime.now().year), attrs=({'style': 'width: 30%; display: inline-block;'})),
        }

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]