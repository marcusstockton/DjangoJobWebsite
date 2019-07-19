from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from Attachment.models import Attachment
# from Company.models import Company
import uuid


class User(AbstractUser):
	class Meta:
		db_table = 'User'
		
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	birth_date = models.DateField(null=True, blank=True, auto_now_add=False)
	attachment = models.ForeignKey(Attachment, null=True, blank=True, on_delete=models.CASCADE)
	alternative_email_address = models.EmailField(null=True, blank=True)
	# company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.username

	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"pk": self.id})
