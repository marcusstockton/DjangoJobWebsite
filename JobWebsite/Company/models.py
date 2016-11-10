from django.db import models
from Address import models as address
# Create your models here.
class Company(models.Model):
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(address.Address)

	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("company:detail", kwargs = { "id": self.id })