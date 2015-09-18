from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, HttpResponseNotFound

from . forms import *
from . models import *

from urlobject import URLObject

import os

# Create your views here.

# formsetfactory example 
def forms(request):
	# formsets
	section_form = SectionForm()
	favorite_subject_form = FavoriteSubjectForm()
	student_form = formset_factory(StudentForm, extra=3)
	multiple_form = MultipleForm(5, "DEAN ARMADA")

	if request.method == 'POST':
		print request.POST
		section_form = SectionForm(request.POST)
		student_form = student_form(request.POST)
		favorite_subject_form = FavoriteSubjectForm(request.POST)
		multiple_form = MultipleForm(5, "DEAN AADA", request.POST)
		if section_form.is_valid() and student_form.is_valid():
			section = section_form.save()
			favorite_subject = favorite_subject_form.save()
			for form in student_form:
				# print form
				m = form.save(commit=False)
				m.section = section
				m.favorite_subject = favorite_subject
				m.save()
				if m == 'None':
					pass
				else:
					pass
					# print m
					# Students.objects.create(section=m, name='DEAN Christian Armada')
			print m
			# n = student_form.save(commit=False)
			# n.section = m
			# n.save()
			# section_form.save()
			# print request.POST
		else:
			print section_form.errors
			print student_form.errors

	template = 'forms.html'
	context_dict = {}
	context_dict['section_form'] = section_form
	context_dict['student_form'] = student_form
	context_dict['multiple_form'] = multiple_form
	context_dict['favorite_subject_form'] = favorite_subject_form
	return render(request, template, context_dict)






# categorizing via foreign keys
# pagination
# search
# integration of all above every request
# xyz, abc, viewing_data

# Method for getting all the not blank get requests
# Used Tuple for multiple returns
def xyz(request, method):
	if method == "POST": request_method = request.POST
	elif method == "GET": request_method = request.GET

	# returns full url
	url = request.scheme
	url += "://"
	url += request.META['HTTP_HOST']
	url += request.get_full_path()

	params = "?"

	for x in request_method:
		if x != 'csrfmiddlewaretoken' and x != 'submit' and x != 'page':
			if request_method[x]:
				params += "&"+x+"="+request_method[x]

	return (params, url)

def abc(request, getparam, model, student):
	if getparam in request.GET:
		param = request.GET[getparam]
		param = {getparam:param}
		param = model.objects.get(**param)
		param = {getparam:param}
		param = student.filter(**param)
		return param
	else:
		param = student.filter()
		return param


# WITH "AND" FILTERING
def viewing_data(request):

	template = 'viewing-data.html'

	student = Students.objects.all()
	section = Section.objects.all()
	favorite_subject = FavoriteSubject.objects.all()
	favorite_number = FavoriteNumber.objects.all()
	students_on_table = 5
	params = ""

	if request.method == 'POST':
		# used for multiple returns
		params, url = xyz(request, "POST")
		params = params.replace(" ", "+")
		return HttpResponseRedirect(url+params)

	if request.method == 'GET':
		if len(request.GET):
			if 'section' in request.GET or 'favorite_subject' in request.GET or 'favorite_number' in request.GET or 'students_on_table' in request.GET:
				# pass
				favorite_subject = set()
				section = set()
				favorite_number = set()

				student = Students.objects.filter()
				student = abc(request, 'section', Section, student)
				student = abc(request, 'favorite_subject', FavoriteSubject, student)
				student = abc(request, 'favorite_number', FavoriteNumber, student)

				# # manipulates number of students displayed 
				if 'students_on_table' in request.GET:
					_students_on_table = request.GET['students_on_table']
					students_on_table = int(_students_on_table)

				for param in student:
					section.add(param.section)
					favorite_subject.add(param.favorite_subject)
					favorite_number.add(param.favorite_number)


	params, url = xyz(request, "GET")
	paginator = Paginator(student, students_on_table)
	page = request.GET.get('page')

	try:
		student = paginator.page(page)
	except PageNotAnInteger:
		student = paginator.page(1)
	except EmptyPage:
		student = paginator.page(paginator.num_pages)

	context_dict = {}
	context_dict['student'] = student
	context_dict['section'] = section
	context_dict['favorite_subject'] = favorite_subject
	context_dict['favorite_number'] = favorite_number
	context_dict['students_on_table'] = range(students_on_table)
	context_dict['params'] = params

	return render(request, template, context_dict)

def viewing_data_2(request):


	# Example USED for AND OR filtering
	# first_set = set()
	# student = Students.objects.filter(section=banana).filter(favorite_subject=math)
	# for x in student:
	# 	first_set.add(x.name)
	# student = Students.objects.filter(section=atis).filter()
	# queryset = Students.objects.filter(reduce(lambda x, y: x | y, [Q(name=item) for item in first_set]))
	# print queryset

	student = Students.objects.all()
	section = Section.objects.all()
	favorite_subject = FavoriteSubject.objects.all()
	favorite_number = FavoriteNumber.objects.all()


	template = 'viewing-data-2.html'
	context_dict = {}
	context_dict['student'] = student
	context_dict['section'] = section
	context_dict['favorite_subject'] = favorite_subject
	context_dict['favorite_number'] = favorite_number
	# context_dict["sample"] = "dean"

	return render(request, template, context_dict)




# Special Codes:
# viewing_data

# Int loopin inside a template
# 	- pass a range() from views.py
# Int incremental inside a template
# 	- use {{ forloop.counter }} inside forloop in the template
# Multiple Returns
# 	- see xyz method
#		-- used tuple in returning