from django.db import models

# Create your models here.
class Section(models.Model):
	section = models.CharField(max_length=100, default=None, null=True)

	def __str__(self):
		return str(self.section)

	# return False rejects unwanted data
	def save(self, *args, **kwargs):
		if self.section == None:
			return False
		super(Section, self).save(*args, **kwargs)


class Students(models.Model):
	name = models.CharField(max_length=100, default=None)
	section = models.ForeignKey(Section)

	def __str__(self):
		return self.name