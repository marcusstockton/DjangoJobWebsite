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
    address_type = forms.ChoiceField(required=True, widget=forms.Select, choices=COMPANY_TYPE)

    class Meta:
        model = Company
        fields = [
            "company_name",
            "address",
        ]

class CompanyEditFormCustom(forms.Form):
    company_name = forms.CharField()
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField()
    address_line_3 = forms.CharField()
    post_code = forms.CharField()
    county = forms.CharField()
    country = forms.CharField()