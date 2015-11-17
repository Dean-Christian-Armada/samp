from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import NotificationSerializer

# Create your models here.
class Notification(SelfPublishModel, models.Model):
	serializer_class = NotificationSerializer
	message = models.TextField()

	def __unicode__(self):
		return self.message