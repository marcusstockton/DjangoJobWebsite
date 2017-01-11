from django.db import models
from django.core.urlresolvers import reverse


class Address(models.Model):
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
		return reverse("address:detail", kwargs={"id": self.id})
