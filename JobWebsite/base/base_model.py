from django.db import models
from User.models import User
import uuid
import datetime


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdby', default=uuid.uuid4)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_modifiedby', null=True, blank=True)

    class Meta:
        abstract = True