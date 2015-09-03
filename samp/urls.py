"""samp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^$', 'samp.views.home'),
    url(r'^snippets/', include('snippets.urls')),
    url(r'^autocomplete-light/', include('auto_complete_light.urls')),
    url(r'^webcam/$', 'django_webcam.views.index'),
    url(r'^save-image/$', 'django_webcam.views.save_image'),
    url(r'^update-image/$', 'django_webcam.views.update_image'),
    url(r'^pdf-report/$', 'pdf_report.views.index'),
    url(r'^pdf-report/landscape/$', 'pdf_report.views.landscape'),
]

# Enables Media
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)