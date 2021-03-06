__author__ = 'Marcus Stockton'
from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, EmailInput, TextInput

from .models import User
from Attachment.models import Attachment


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

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		self.fields['birth_date'].widget = TextInput( attrs={'class': 'datepicker','placeholder': 'D.O.B', 'autocomplete':'off'})
		self.fields['email'].widget = EmailInput()

	def save(self, commit=False):
		new_user = User.objects.create_user(
			self.cleaned_data['username'],
			email=self.cleaned_data['email'],
			password=self.cleaned_data['password1'],
			first_name=self.cleaned_data['first_name'],
			last_name=self.cleaned_data['last_name'],
			birth_date=self.cleaned_data['birth_date'],
		)
		attachment = Attachment.objects.create(
			avatar=self.cleaned_data['avatar'],
			cv=self.cleaned_data['cv'],
			User=new_user)
		new_user.attachment = attachment
		new_user.save()
		attachment.save()
		return new_user

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
										   attrs=({'style': 'width: 30%; display: inline-block; class: datepicker'})),
			"email": EmailInput(),
			"first_name": TextInput(attrs={'style': 'text-transform:capfirst;'})
		}

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get("username")
		email = cleaned_data.get("email")
		first_name = cleaned_data.get("first_name")
		last_name = cleaned_data.get("last_name")
		birth_date = cleaned_data.get("birth_date")


class UserLoginForm(ModelForm):
	class Meta:
		model = User
		fields = [
			"username",
			"password"
		]
