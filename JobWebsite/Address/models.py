from django.db import models
from django.urls import reverse
import uuid


class Address(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	address_type = models.CharField(max_length=20)
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
