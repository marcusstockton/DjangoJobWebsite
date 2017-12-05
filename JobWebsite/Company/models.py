from django.db import models
from Address.models import Address
from django.urls import reverse


class Company(models.Model):
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("companies:detail", kwargs = { "pk": self.pk })