from django.db import models
from Address.models import Address
from django.core.urlresolvers import reverse


class Company(models.Model):
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(Address)

	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("companies:detail", kwargs = { "pk": self.pk })