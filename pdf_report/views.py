from django.shortcuts import render
from django.http import HttpResponse

# from reportlab.pdfgen import canvas
# from django_xhtml2pdf.utils import generate_pdf
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

# Create your views here.
def index(request):
	# return render(request, 'pdf.html', {})
	template = "pdf.html"
	# returns hypertext protocol: http or https
	domain = request.scheme
	domain += "://"
	# returns domain name
	domain += request.META["HTTP_HOST"]
	context_dict = {"domain":domain}
	return render_to_pdf_response(request, template, context_dict)
	# template_name = "hello.html"
	# resp = HttpResponse(content_type='application/pdf')
	# result = generate_pdf('pdf.html', file_object=resp)
	# return result

def landscape(request):
	# return render(request, 'pdf.html', {})
	template = "pdf-landscape.html"
	# returns hypertext protocol: http or https
	domain = request.scheme
	domain += "://"
	# returns domain name
	domain += request.META["HTTP_HOST"]
	context_dict = {"domain":domain}
	return render_to_pdf_response(request, template, context_dict)
	# template_name = "hello.html"
	# resp = HttpResponse(content_type='application/pdf')
	# result = generate_pdf('pdf.html', file_object=resp)
	# return result