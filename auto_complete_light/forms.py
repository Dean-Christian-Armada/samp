from django import forms

from snippets.models import *

import autocomplete_light

class SectionModelForm(autocomplete_light.ModelForm):
	name = forms.CharField(widget=autocomplete_light.TextWidget('SectionAutocomplete', attrs={'placeholder':'Search Name'}))
	class Meta:
		model = Students
		fields = ('name', )
