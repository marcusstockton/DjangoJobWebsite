from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

def __str__(self):
	return self.title


def get_absolute_url(self):
	return reverse("users:detail", kwargs={"pk": self.id})
