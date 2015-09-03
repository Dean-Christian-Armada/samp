from django.db import models

from django_date_extensions.fields import *

# Input March 1963 on admin
# Resource: http://nullege.com/codes/search/django_date_extensions.fields.ApproximateDateField
# 			https://github.com/dracos/django-date-extensions

# Create your models here.

class SampleMonthDate(models.Model):
	birthdate = ApproximateDateField(default=None)
	date = models.DateField(default=None)