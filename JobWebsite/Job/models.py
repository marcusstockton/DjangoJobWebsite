from django.db import models
from django.urls import reverse
from User.models import User
import uuid


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:detail", kwargs={"pk": self.pk})


class JobApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="job_applicant")
    # Save the cv incase user updates cv after application
    applicant_cv = models.FileField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    job_owner = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="job_owner")

    def __str__(self):
            return self.job + ": " + self.applicant.name

    def get_absolute_url(self):
        return reverse("jobs:jobapplication", kwargs={"pk": self.pk})
