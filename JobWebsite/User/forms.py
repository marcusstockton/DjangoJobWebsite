__author__ = 'Marcus Stockton'
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget

class CustomUserCreationForm(UserCreationForm):
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


class UserForm(forms.ModelForm):
	birth_date = forms.DateField(widget=SelectDateWidget(years=range(1925, 2100), empty_label=("Choose Year", "Choose Month", "Choose Day")))
	#birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
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

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			"username",
			"password"
		]