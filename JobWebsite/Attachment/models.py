from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attachment(models.Model):
	file_name = models.CharField(max_length=120)
	data = models.BinaryField()
	created_date = models.DateField(auto_now_add=True)
	file_type = models.CharField(max_length=120)
	active = models.BooleanField()
	User = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("attachments:detail", kwargs = { "pk": self.id })