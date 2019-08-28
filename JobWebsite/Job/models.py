from django.db import models
from django.urls import reverse
from User.models import User
from Attachment.models import Attachment
from base.base_model import BaseModel
import uuid


class JobType(BaseModel, models.Model):
	class Meta:
		db_table = 'JobType'
	description = models.TextField(max_length = 50) # contract, permanent

	def __str__(self):
		return self.description
		

class JobPosistion(BaseModel, models.Model):
	class Meta:
		db_table = 'JobPosistion'
	description = models.TextField(max_length = 50) # full time, part time

	def __str__(self):
		return self.description



class JobCategory(BaseModel, models.Model):
	class Meta:
		db_table = 'JobCategory'
	description = models.TextField(max_length = 50) # IT, Sales

	def __str__(self):
		return self.description


class JobKeySkills(BaseModel, models.Model):
	class Meta:
		db_table = 'JobKeySkills'
	description = models.TextField(max_length = 50) # C++ / Python / OpenCV / OpenGL / TensorFlow
	
	def __str__(self):
		return self.description


class JobBenefits(BaseModel, models.Model):
	class Meta:
		db_table = 'JobBenefits'
	description = models.TextField(max_length = 50) # Pension / Cycle To Work scheme / 

	def __str__(self):
		return self.description


class Job(BaseModel, models.Model):
	class Meta:
		db_table = 'Job'
		
	title = models.CharField(max_length=120)
	content = models.TextField(max_length=2000)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	min_salary = models.IntegerField()
	max_salary = models.IntegerField()
	closing_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
	primary_location = models.CharField(max_length=2000, null=True) # this should / will be a drop down list...
	category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, related_name="job_category", null=True)
	job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, related_name="job_type", null=True)
	key_skills = models.ManyToManyField(JobKeySkills, related_name="job_key_skills", null=True)

	def __str__(self):
	    return '%s %s' % (self.title, self.publish)

	def get_absolute_url(self):
		return reverse("jobs:detail", kwargs={"pk": self.pk})


class JobApplication(BaseModel,models.Model):
	class Meta:
		db_table = 'JobApplication'

	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_applicant")
	applicant_cv = models.ForeignKey(Attachment, on_delete=models.CASCADE)
	job_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_owner")

	def __repr__ (self):
			return self.job.title + ": " + self.applicant.username

	def get_absolute_url(self):
		return reverse("jobs:jobapplication", kwargs={"pk": self.pk})


