from django.shortcuts import render
from registration.backends.default.views import RegistrationView
from invite.models import MyRegistrationForm
from django.contrib.auth.models import User
from invite.models import Invitation

class RegistrationViewUniqueEmail(RegistrationView):
    form_class = MyRegistrationForm
