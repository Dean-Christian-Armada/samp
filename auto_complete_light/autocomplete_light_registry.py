# from django.utils.translation import ugettext_lazy as _

from snippets.models import *

import autocomplete_light


class SectionAutocomplete(autocomplete_light.AutocompleteModelTemplate):
    search_fields = ['^name', ]
    model = Students
    # Template that removes the "Results not Found"
    autocomplete_template = 'autocomplete_template.html'
    

    # autocomplete_html_format = u'<span class="autocomplete-os">%s</span>'

    # With Get PARAMETERS
    # Use Jquery or Views to manipulate the autocompletefield
    # MANIPULATE data-autocomplete-url
    # def choices_for_request(self):
    # 	if 'section' in self.request.GET:
	   #  	section = self.request.GET['section']
	   #  	section = Section.objects.get(section=section)
	   #  	self.choices = self.choices.filter(section=section)
    # 	return super(SectionAutocomplete, self).choices_for_request()

autocomplete_light.register(SectionAutocomplete)