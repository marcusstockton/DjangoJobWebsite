import json
import urllib.request

from django import forms

from .models import Address, AddressType


def get_countries():
	url = "http://country.io/names.json"
	req = urllib.request.Request(url)
	r = urllib.request.urlopen(req).read()
	cont = json.loads(r)
	return sorted(cont.items(), key=lambda x: x[1])
	# Might be worth looking at http://battuta.medunes.net/


class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = "__all__"
		localized_fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(AddressForm, self).__init__(*args, **kwargs)
		self.fields['address_type'].queryset = AddressType.objects.filter(is_active=True)
		self.fields['country'] = forms.ChoiceField(choices=get_countries())

	def clean_address_line_1(self):
		address_line_1 = self.cleaned_data['address_line_1']
		return address_line_1

	def clean_address_line_2(self):
		address_line_2 = self.cleaned_data['address_line_2']
		return address_line_2

	def clean_address_line_3(self):
		address_line_3 = self.cleaned_data['address_line_3']
		return address_line_3

	def clean_post_code(self):
		post_code = self.cleaned_data['post_code']
		return post_code

	def clean_county(self):
		county = self.cleaned_data['county']
		return county

	def clean_country(self):
		country = self.cleaned_data['country']
		return country
