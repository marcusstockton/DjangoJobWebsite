from django import forms
from django.forms.widgets import Select
import requests
import yaml
from .models import Company


def get_company_data():
	url = 'https://raw.githubusercontent.com/companieshouse/api-enumerations/master/constants.yml'
	data = requests.get(url)
	if data.status_code == 200:
		yaml_data = yaml.safe_load(data.text)

		nature_of_business = yaml_data['sic_descriptions']
		company_type = yaml_data['company_type']

		results = {
			'nature_of_business': nature_of_business,
			'company_type': company_type
		}
		return results
	return []


class CompanyForm(forms.ModelForm):
	nature_of_business = forms.CharField(label='Nature of Business')
	company_type = forms.CharField(label='Company Type')

	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
			'nature_of_business',
			'company_type'
		]
		localized_fields = "__all__"
	
	def __init__(self, *args, **kwargs):
		super(CompanyForm, self).__init__(*args, **kwargs)

		company_data = get_company_data()
		nob = company_data['nature_of_business']
		ct = company_data['company_type']

		self.fields['nature_of_business'].widget = Select(choices=nob.items())
		self.fields['company_type'].widget= Select(choices=ct.items())

		


class CompanyEditForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = [
			"company_name",
			'nature_of_business',
			'company_type'
		]
		localized_fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(CompanyEditForm, self).__init__(*args, **kwargs)

		instance = kwargs.get('instance')
		company = instance
		address = instance.address

		company_data = get_company_data()
		nob = company_data['nature_of_business']
		ct = company_data['company_type']

		self.fields['nature_of_business'].widget = Select(choices=nob.items())
		self.fields['nature_of_business'].initial = nob[instance.nature_of_business]

		self.fields['company_type'].widget= Select(choices=ct.items())
		self.fields['company_type'].initial = ct[instance.company_type]
		
