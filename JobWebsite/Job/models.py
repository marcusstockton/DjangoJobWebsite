from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Job(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField(max_length=2000)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("jobs:detail", kwargs = { "pk": self.pk })