__author__ = 'Marcus Stockton'
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField()
	email = forms.CharField( widget=forms.EmailInput)
	password = forms.CharField( widget=forms.PasswordInput)
	first_name = forms.CharField()
	last_name = forms.CharField()
	birth_date = forms.CharField( widget=forms.DateInput)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('birth_date',)


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
