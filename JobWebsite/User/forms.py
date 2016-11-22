__author__ = 'Marcus Stockton'
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('birth_date','first_name', 'last_name', 'email')


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
			"first_name",
			"last_name",
			"birth_date"
		]
