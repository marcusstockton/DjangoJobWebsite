from django import forms
from django.forms import ModelForm, widgets
from .models import Attachment

class AttachmentForm(ModelForm):
    
	class Meta:
		model = Attachment
		fields = [
			"avatar",
			"cv",
			#"created_date"
		]
		localized_fields = "__all__"

		widgets={
            'avatar': widgets.ClearableFileInput,
            'cv': forms.ClearableFileInput(),
        }
		#readonly_fields = ('created_date',)