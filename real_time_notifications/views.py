from django.shortcuts import render
from django.views.generic import ListView

from .models import Notification

# Create your views here.
def Notifications(request):
	# model = Notification
	template_name = 'real-time-notifications.html'
	object_list = Notification.objects.filter()
	context_dict = {'object_list' : object_list}
	
	return render(request, template_name, context_dict)

	# def get_queryset(self):
	# 	return self.model.objects.order_by('-pk')[:5]