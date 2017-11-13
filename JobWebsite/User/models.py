from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from Attachment.models import Attachment

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True, auto_now_add=False)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.id})
