from django import forms
from .models import Company
from Address.models import AddressType


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
		]
		localized_fields = "__all__"


class CompanyEditForm(forms.ModelForm):
	address_type = forms.ModelChoiceField(queryset=AddressType.objects.filter(is_active=True), empty_label=None)

	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
			"address_type"
		]

	def __init__(self, *args, **kwargs):
		super(CompanyEditForm, self).__init__(*args, **kwargs)
		company = kwargs.get('instance')
		self.fields['address_type'].initial = company.address.address_type