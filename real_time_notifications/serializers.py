from swampdragon.serializers.model_serializer import ModelSerializer

# from .models import Notification

class NotificationSerializer(ModelSerializer):
	class Meta:
		model = 'real_time_notifications.Notification'
		publish_fields = ['message']