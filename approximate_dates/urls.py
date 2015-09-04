from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^month-year/', views.month_year, name='month-year'),
]