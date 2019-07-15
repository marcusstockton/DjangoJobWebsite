from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
		]
		localized_fields = "__all__"


class CompanyEditForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = [
			"company_name",
		]
		localized_fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(CompanyEditForm, self).__init__(*args, **kwargs)
		instance = kwargs.get('instance')
		company = instance
		address = instance.address
