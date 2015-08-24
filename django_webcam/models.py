from django.db import models

class Picture(models.Model):
	name = models.CharField(max_length=100, null=True)
	picture = models.ImageField(upload_to='pictures', blank=True)