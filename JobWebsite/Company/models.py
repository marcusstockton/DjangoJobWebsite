from django.db import models
from django.urls import reverse

from Address.models import Address
from base.base_model import BaseModel


class Company(BaseModel, models.Model):
	class Meta:
		db_table = 'Company'
		
	company_name = models.CharField(max_length=200)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	nature_of_business = models.CharField(max_length=200, null=True) # https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/527619/SIC07_CH_condensed_list_en.csv/preview
	company_type = models.CharField(max_length=100, null=True) # https://www.companyaddress.co.uk/post/38
	# maybe read this yaml file :# https://github.com/companieshouse/api-enumerations/blob/master/constants.yml and parse out the info...?

	#parent_company = models.ForeignKey("Company", null=True, blank=True)


	def __str__(self):
			return self.company_name

	def get_absolute_url(self):
		return reverse("companies:detail", kwargs={"pk": self.pk})
