from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from Attachment import models as attachment

class User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)
	attachments = models.ForeignKey(attachment.Attachment, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"pk": self.id})
