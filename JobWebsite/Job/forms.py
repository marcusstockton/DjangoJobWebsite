from django import forms
from django.forms import ModelForm, widgets
from .models import Job
from datetime import datetime


class JobForm(ModelForm):

    class Meta:
        model = Job
        fields = [
            "title",
            "content",
            "publish"
        ]
        localized_fields = "__all__"
        widgets = {
            "publish": widgets.SelectDateWidget(
                years=range(datetime.now().year,
                            datetime.now().year + 5),
                attrs=({'style': 'width: 30%; display: inline-block;'})),
        }


class JobApplyForm(forms.Form):
    attachment = forms.FileField()
    job_title = forms.CharField(widget=forms.TextInput(
        attrs={"readonly": "readonly"}))
    current_attachment = forms.CharField(max_length=500,
                                         widget=forms.TextInput(
                                             attrs={"readonly": "readonly"}))
    user_email_address = forms.EmailField(
        widget=forms.TextInput(
            attrs={"readonly": "readonly"}))

    def clean_attachment(self):
        attachment = self.cleaned_data['attachment']
        return attachment
