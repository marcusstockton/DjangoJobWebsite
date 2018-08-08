from django.db import models
from Address.models import Address
from django.urls import reverse
import uuid


class Company(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4,
	                      editable=False, unique=True)
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)

	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("companies:detail", kwargs={"pk": self.pk})
