from django import forms

from .models import Company

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = [
			"company_name",
			"address",
		]

FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

class CompanyEditForm(forms.Form):
	favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select,
        choices=FAVORITE_COLORS_CHOICES,
   )
	company_name = forms.CharField(max_length=200)
	address_line_1 = forms.CharField(max_length=200)
	address_line_2 = forms.CharField(max_length=200)
	address_line_3 = forms.CharField(max_length=200)
	town = forms.CharField(max_length=200)