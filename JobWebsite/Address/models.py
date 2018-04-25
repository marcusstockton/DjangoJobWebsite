from django.db import models
from django.urls import reverse
import uuid


class Address(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	address_type = models.ForeignKey('AddressType', on_delete=models.CASCADE, blank=False, null=False)
	address_line_1 = models.CharField(max_length=2000)
	address_line_2 = models.CharField(max_length=50, blank=True, null=True)
	address_line_3 = models.CharField(max_length=50, blank=True, null=True)
	post_code = models.CharField(max_length=10)
	county = models.CharField(max_length=20)
	country = models.CharField(max_length=20)

	def __str__(self):
		return self.address_line_1

	def get_absolute_url(self):
		return reverse("addresses:detail", kwargs={"pk": self.id})


class AddressType(models.Model):
		id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
		description = models.CharField(max_length=50)
		is_active = models.BooleanField(default=True)

		def __str__(self):
				return self.description

		def get_absolute_url(self):
				return reverse("addressType:detail", kwargs={"pk": self.id})
