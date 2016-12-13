from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Attachment(models.Model):
	file_name = models.CharField(max_length=120)
	data = models.BinaryField()
	created_date = models.DateField(auto_now_add=True)
	file_type = models.CharField(max_length=120)
	active = models.BooleanField()
	User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.file_name

	def get_absolute_url(self):
		return reverse("attachments:detail", kwargs = { "pk": self.id })

def handle_uploaded_file(instance, file):
	user_dir = djangoSettings.STATIC_ROOT + '/' + instance.username + "/" + file.name
	with open(user_dir, 'wb+') as destination:
		for chunk in file.chunks():
			destination.write(chunk)
