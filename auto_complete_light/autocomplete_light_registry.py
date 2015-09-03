from snippets.models import *
import autocomplete_light


class SectionAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^name', ]
    model = Students
autocomplete_light.register(SectionAutocomplete)