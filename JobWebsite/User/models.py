from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

def upload_location(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
	birth_date = models.DateField(null=True, blank=True)
	avatar = models.ImageField(upload_to=upload_location, null=True, blank=True)
	cv = models.FileField(upload_to=upload_location, blank=True)
	
	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"pk": self.id})
