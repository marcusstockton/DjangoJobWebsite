__author__ = 'Marcus Stockton'
from django import forms
from .models import User


class UserCreationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username", "email", "password", "first_name", "last_name", "birth_date")