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

COMPANY_TYPE = (
    ('Res', 'Residential'),
    ('Bus', 'Business'),
)

class CompanyEditForm(forms.ModelForm):
	address_type = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=COMPANY_TYPE,
   )
	# company_name = forms.CharField(max_length=200)
	# address_line_1 = forms.CharField(max_length=200)
	# address_line_2 = forms.CharField(max_length=200)
	# address_line_3 = forms.CharField(max_length=200)
	# town = forms.CharField(max_length=200)
	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
		]