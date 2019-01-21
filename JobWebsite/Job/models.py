from django.db import models
from django.urls import reverse
from User.models import User
from Attachment.models import Attachment
from base.base_model import BaseModel
import uuid


class Job(BaseModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    publish = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"pk": self.pk})


class JobApplication(BaseModel,models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_applicant")
    applicant_cv = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    job_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_owner")

    def __repr__ (self):
            return self.job.title + ": " + self.applicant.username

    def get_absolute_url(self):
        return reverse("jobs:jobapplication", kwargs={"pk": self.pk})
