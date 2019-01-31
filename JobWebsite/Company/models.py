from django.db import models
from django.urls import reverse

from Address.models import Address
from base.base_model import BaseModel


class Company(BaseModel, models.Model):
	class Meta:
		db_table = 'Company'
		
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("companies:detail", kwargs={"pk": self.pk})
