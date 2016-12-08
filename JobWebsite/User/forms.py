__author__ = 'Marcus Stockton'
from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('birth_date',
			'first_name', 
			'last_name', 
			'email', 
			"avatar",
			"cv"
		)

# get an array of years for 80? years from current year:
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990')

class UserForm(forms.ModelForm):
	birth_date = forms.CharField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
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
