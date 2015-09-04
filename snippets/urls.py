from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^forms/', views.forms, name='forms'),
    url(r'^viewing-data/$', views.viewing_data, name='viewing_data'),
    url(r'^viewing-data/2/$', views.viewing_data_2, name='viewing_data_2'),
]