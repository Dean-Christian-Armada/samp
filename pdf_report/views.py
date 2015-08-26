from django.shortcuts import render
from django.http import HttpResponse

# from reportlab.pdfgen import canvas
# from django_xhtml2pdf.utils import generate_pdf
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

# Create your views here.
def index(request):
	# return render(request, 'pdf.html', {})
	return render_to_pdf_response(request, 'pdf.html', {})
	# template_name = "hello.html"
	# resp = HttpResponse(content_type='application/pdf')
	# result = generate_pdf('pdf.html', file_object=resp)
	# return result