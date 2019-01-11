from django.db import models
from User.models import User
import uuid

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdby')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_modifiedby', null=True, blank=True)

    class Meta:
        abstract = True