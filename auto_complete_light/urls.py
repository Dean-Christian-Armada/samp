from django.conf.urls import include, url
from django.contrib import admin

from . import views

import autocomplete_light.shortcuts
import autocomplete_light

from . autocomplete_light_registry import *


urlpatterns = [
    url(r'^forms/', views.forms, name='autocomplete-forms'),
]