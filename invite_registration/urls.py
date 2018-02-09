# -*- coding: utf-8 -*-
from invite_registration import views
from django.conf.urls import url

urlpatterns = [
    url(r'^invite/$', views.invite, name="invite_invite"),
    url(r'^request/$', views.request_invite, name="invite_request"),
]
