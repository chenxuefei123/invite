# -*- coding: utf-8 -*-
from invite_registration import views  
from django.conf.urls import url

urlpatterns = [
    url(r'^invite/$', views.invite, name='invitation_invite'), 
    url(r'^request/$', views.request_invite, name='invitation_request'),        
]
