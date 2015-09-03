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