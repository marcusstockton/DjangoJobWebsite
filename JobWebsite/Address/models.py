from django.db import models

# Create your models here.
class Address(models.Model):
	address_type = models.IntField()
	address_line_1 = models.TextField(max_length=2000)
	address_line_2 = models.TextField(blank=True, null=True)
	address_line_3 = models.TextField(blank=True, null=True)
	post_code = models.TextField(max_length=10)
	county = models.TextField(max_length=20)
	country = models.TextField(max_length=20)

	def __str__(self):
			return self.address_line_1

	def get_absolute_url(self):
		return reverse("address:detail", kwargs = { "id": self.id })