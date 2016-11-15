from django import forms

from .models import Address


COMPANY_TYPE = (
    ('Res', 'Residential'),
    ('Bus', 'Business'),
)

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
			"address_type",
			"address_line_1",
			"address_line_2",
			"address_line_3",
			"post_code",
			"county",
			"country"
		]

class AddressEditForm(forms.ModelForm):
	address_type = forms.ChoiceField(
        required=True,
        widget=forms.Select,
        choices=COMPANY_TYPE,
   )
	class Meta:
		model = Address
		fields = [
			"address_type",
			"address_line_1",
			"address_line_2",
			"address_line_3",
			"post_code",
			"county",
			"country"
		]	