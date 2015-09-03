def viewing_data(request):

	template = 'viewing-data.html'

	student = Students.objects.all()
	section = Section.objects.all()
	favorite_subject = FavoriteSubject.objects.all()
	favorite_number = FavoriteNumber.objects.all()
	students_on_table = 5
	params = ""

	if request.method == 'POST':
		# returns full url
		url = request.scheme
		url += "://"
		url += request.META['HTTP_HOST']
		url += request.get_full_path()

		params = "?"

		for x in request.POST:
			if x != 'csrfmiddlewaretoken' and x != 'submit':
				if request.POST[x]:
					params += "&"+x+"="+request.POST[x]

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
				if 'section' in request.GET:
					# pass
					_section = request.GET['section']
					_section = Section.objects.get(section=_section)
					student = student.filter(section=_section)
					# FOR OR FILTERING
					# for subjects in student: 
					# 	_subjects.add(subjects.favorite_subject)
					# favorite_subject = _subjects
				
				# student = abc(request, 'section', Section, student)
				# student = abc(request, 'favorite_subject', FavoriteSubject, student)
				# student = abc(request, 'favorite_number', FavoriteNumber, student)

				if 'favorite_subject' in request.GET:
					_subject = request.GET['favorite_subject']
					_subject = FavoriteSubject.objects.get(favorite_subject=_subject)
					student = student.filter(favorite_subject=_subject)
					# FOR OR FILTERING
					# for sections in student: 
					# 	_sections.add(sections.section)
					# section = _sections
				if 'favorite_number' in request.GET:
					# pass
					_number = request.GET['favorite_number']
					_number = FavoriteNumber.objects.get(favorite_number=_number)
					student = student.filter(favorite_number=_number)

				# # manipulates number of students displayed 
				if 'students_on_table' in request.GET:
					_students_on_table = request.GET['students_on_table']
					students_on_table = int(_students_on_table)
					print students_on_table
					# student = student[:_students_on_table]

				print "Dean"
				print student
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

	# Shows the length of the students within the table
	

	context_dict = {}
	context_dict['student'] = student
	context_dict['section'] = section
	context_dict['favorite_subject'] = favorite_subject
	context_dict['favorite_number'] = favorite_number
	context_dict['students_on_table'] = range(students_on_table)
	context_dict['params'] = params

	return render(request, template, context_dict)