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

class FavoriteSubject(models.Model):
	favorite_subject = models.CharField(max_length=100, default=None)

	def __unicode__(self):
		return self.favorite_subject

class FavoriteNumber(models.Model):
	favorite_number = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return unicode(self.favorite_number)

class Students(models.Model):
	name = models.CharField(max_length=100, default=None)
	section = models.ForeignKey(Section)
	favorite_subject = models.ForeignKey(FavoriteSubject)
	favorite_number = models.ForeignKey(FavoriteNumber, default=1)

	def __str__(self):
		return self.name

	def x(self):
		return self.name+"dean"

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True

# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)