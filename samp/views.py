from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def home(request):
	# return HttpResponse("DEAN")
	template = 'home.html'
	context_dict = {}
	return render(request, template, context_dict)