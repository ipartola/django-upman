from __future__ import print_function, division, absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^uploads$', views.uploads, name='upman-uploads'),
    url(r'^image-uploads$', views.image_uploads, name='upman-image-uploads'),
]
