from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class EmailNotification(models.Model):
	status = RichTextField()
	greetings = RichTextField()
	message = RichTextField()

	def __unicode__(self):
		return "%s" % self.greetings