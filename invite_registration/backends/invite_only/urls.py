# -*- coding: utf-8 -*-
"""
URLconf for registration and activation, using invite_registration backend.

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize the behavior (e.g., by passing extra
arguments to the various views) or split up the URLs, feel free to set
up your own URL patterns for these views instead.

"""

from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from registration.views import RegistrationView

urlpatterns = [
    url(r'^register/$',
        RegistrationView,
        name='registration_register'),
    path('register/closed/',
         TemplateView.as_view(template_name='registration/registration_closed.html'),
         name="registration_disallowed"),
    path('', include('registration.auth_urls')),
]
