from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from Attachment.models import Attachment
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birth_date = models.DateField(null=True, blank=True, auto_now_add=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.id})
