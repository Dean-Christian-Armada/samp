from django import forms

from . models import *

class StudentForm(forms.ModelForm):
	class Meta:
		model = Students
		fields = ('name', )

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = ('section', )

class FavoriteSubjectForm(forms.ModelForm):
	class Meta:
		model = FavoriteSubject
		fields = ('favorite_subject', )

class MultipleForm(forms.Form):
	atis = Section.objects.get(section='Atis')
	sections = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Students.objects.filter(section=atis), required=False)
	
	def __init__(self, id, name, *args, **kwargs):
		print id
		print name

		super(MultipleForm, self).__init__(*args, **kwargs)
