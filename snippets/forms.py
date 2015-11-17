from django.forms.formsets import BaseFormSet
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

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = ('section', )

class DynamicFolderPicture(forms.ModelForm):
	class Meta:
		model = NamePicture
		fields = ('name', 'folder_path', 'picture')

class FooForm(forms.Form):
	x = forms.CharField()
	def __init__(self, province_id, city_id, *args, **kwargs):
		print province_id
		print city_id
		super(FooForm, self).__init__(*args, **kwargs)

class FirstRequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(FirstRequiredFormSet, self).__init__(*args, **kwargs)
        self.forms[0].empty_permitted = False