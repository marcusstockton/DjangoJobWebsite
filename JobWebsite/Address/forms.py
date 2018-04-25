from django import forms

from .models import Address, AddressType


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
		localized_fields = "__all__"

	def __init__(self, user, *args, **kwargs):
		super(AddressForm, self).__init__(*args, **kwargs)
		self.fields['address_type'].queryset = AddressType.objects.filter(is_active=True) # Limit select list to active options