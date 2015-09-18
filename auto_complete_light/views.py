from django.shortcuts import render
from django.http import HttpResponse

from . forms import *

# Create your views here.

# Steps
# Create autcomplete_light_registry.py(same directory) with the date storage syntax
# Create an autocomplete_light.TextWidget() on your Form with the attributes of the class created on the autcomplete_light_registry.py
# implement the form on the views and template 
# "autocomplete_light.ModelForm" - please do not forget to inherit this next time in forms
# make sure to include {% include 'autocomplete_light/static.html' %}
# make sure to include "url(r'^autocomplete/', include('autocomplete_light.urls'))" in the project's urls.py
# Test the app it should be working

# Best Resource: http://stackoverflow.com/questions/20081629/cant-get-django-autocomplete-light-to-work-outside-model-form

def forms(request):
	form = SectionModelForm()
	template = "autocomplete_light.html"
	context_dict = {'form':form}
	return render(request, template, context_dict)
	# return HttpResponse("dadads")
