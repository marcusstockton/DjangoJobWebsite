from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class User(AbstractUser):
	birth_date = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"pk": self.id})
