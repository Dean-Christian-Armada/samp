from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from . models import Picture

import os, random

# Create your views here.
def index(request):
	# camera_form = CameraForm()
	template = 'camera.html'
	context_dict = {}
	# context_dict['camera_form'] = camera_form
	return render(request, template, context_dict)

@csrf_exempt
def save_image(request):
	if request.method == 'POST':
		print "dean"
		# does not work with starting slash
		x = 'media/pictures/tmp/someimage.jpg'
		# y = 'media/pictures/someimage.jpg'
		f = open(x, 'wb')
		f.write(request.body)
		f.close()
		# os.rename(x, y)
		return HttpResponse(request.scheme+"://"+request.META['HTTP_HOST']+"/"+x)
	else:
		return HttpResponse("No data")

def update_image(request):
	if request.method == 'POST':
		picture = "pictures/"+request.POST['update_image']+".jpg"
		print picture
		x = 'media/tmp/someimage.jpg' 
		y = 'media/pictures/image.jpg'
		os.rename(x, y)
		picture = Picture.objects.create(name='Dean Armada', picture=picture)
	return HttpResponseRedirect('/webcam/')