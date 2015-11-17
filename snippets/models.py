from django.db import models
import os

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

# A scipt used for dynamic folders in picture file upload
def content_file_name(instance, filename):
    upload_dir = os.path.join('dynamic-folder-pictures',instance.folder_path.name)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

# Use "/" as a part of the name for sub-folder
class PictureFolders(models.Model):
	name = models.CharField(max_length=50, default=None)

	def __str__(self):
		return self.name

class NamePicture(models.Model):
	name = models.CharField(max_length=50, default=None)
	# job = models.CharField(max_length=50, default=None)
	folder_path = models.ForeignKey(PictureFolders, default=None)
	picture = models.ImageField(upload_to=content_file_name, blank=True)

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True

# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)