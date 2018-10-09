__author__ = 'Marcus Stockton'
from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, EmailInput

from .models import User


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
        localized_fields = "__all__"


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
        localized_fields = "__all__"
        widgets = {
            "birth_date": SelectDateWidget(years=range(1900, datetime.now().year),
                                           attrs=({'style': 'width: 30%; display: inline-block;'})),
            "email": EmailInput(),
        }

    def clean(self):
        super().clean()


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]
