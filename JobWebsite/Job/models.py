from django.db import models
from django.urls import reverse
from User.models import User
from Attachment.models import Attachment
from base.base_model import BaseModel
import uuid


class JobType(BaseModel, models.Model):
	class Meta:
		db_table = 'JobType'
	description = models.CharField(max_length = 50) # contract, permanent

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('jobs:jobtype-details', kwargs={'pk': self.pk})
		

class JobPosistion(BaseModel, models.Model):
	class Meta:
		db_table = 'JobPosistion'
	description = models.CharField(max_length = 50) # full time, part time

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('jobs:jobposistion-details', kwargs={'pk': self.pk})


class JobCategory(BaseModel, models.Model):
	class Meta:
		db_table = 'JobCategory'
	description = models.CharField(max_length = 50) # IT, Sales

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('jobs:jobcategory-details', kwargs={'pk': self.pk})

class JobKeySkills(BaseModel, models.Model):
	class Meta:
		db_table = 'JobKeySkills'
	description = models.CharField(max_length = 50) # C++ / Python / OpenCV / OpenGL / TensorFlow
	
	def __str__(self):
		return self.description
	
	def get_absolute_url(self):
		return reverse('jobs:jobkeyskills-details', kwargs={'pk': self.pk})


class JobBenefits(BaseModel, models.Model):
	class Meta:
		db_table = 'JobBenefits'
	description = models.CharField(max_length = 50) # Pension / Cycle To Work scheme / 

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('jobs:jobbenefits-details', kwargs={'pk': self.pk})

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


