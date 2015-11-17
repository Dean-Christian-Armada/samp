try:
    from people.asynchronous_mail import send_mail
except:
    from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import Context, Template
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from . models import EmailNotification


# rendered = Template("{% load your_tag_library %}",
#     object.textfield).render(Context())

# Create your views here.
def email_check(request):
	email = 'adgc.manship@gmail.com'
	x = EmailNotification.objects.filter()[0]
	# rendered = Template("{'name': 'Dean Armada'}", x.greetings).render(Context())
	template = 'variables_inside_model_text_field.html'
	status_template = Template(x.status)
	status = Context({})
	status = status_template.render(status)

	greetings_template = Template(x.greetings)
	greetings = Context({'name': 'Dean Christian Armada', 'count': 1000})
	greetings = greetings_template.render(greetings)

	message_template = Template(x.message)
	message = Context({'age': '23'})
	message = message_template.render(message)

	context_dict = {}
	context_dict['status'] = status
	context_dict['greetings'] = greetings
	context_dict['message'] = message
	# email_data = {}
	# msg_plain = render_to_string('email-templates/mariner-passed.txt', context_dict)
	# ALSO in email function
	msg_html = render_to_string('email-templates/mariner-passed.html', context_dict)
	msg_plain = "PLAIN"
	# msg_html = "HTML"
	send_mail('Sample Title', msg_plain, settings.EMAIL_HOST_USER, [email], fail_silently=False, html_message=msg_html)

	return render(request, template, context_dict)