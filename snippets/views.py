from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import *

# Create your views here.

def forms(request):
	# formsets
	student_form = StudentForm()
	section_form = formset_factory(SectionForm, extra=3)

	if request.method == 'POST':
		print request.POST
		student_form = StudentForm(request.POST)
		section_form = section_form(request.POST)
		if section_form.is_valid() and student_form.is_valid():
			for form in section_form:
				# print form
				m = form.save()
				if m == 'None':
					pass
				else:
					pass
					# print m
					# Students.objects.create(section=m, name='DEAN Christian Armada')
			print m
			n = student_form.save(commit=False)
			n.section = m
			n.save()
			# section_form.save()
			# print request.POST
		else:
			print section_form.errors
			print student_form.errors

	template = 'forms.html'
	context_dict = {}
	context_dict['section_form'] = section_form
	context_dict['student_form'] = student_form
	return render(request, template, context_dict)
