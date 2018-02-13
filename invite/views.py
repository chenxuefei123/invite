from django.shortcuts import render
from registration.backends.default.views import RegistrationView
from invite.models import MyRegistrationForm
from django.contrib.auth.models import User
from invite.models import Invitation
from datetime import datetime

class RegistrationViewInvite(RegistrationView):
    form_class = MyRegistrationForm
    def register(self, form):
        # save a record
        try:
            invitor_obj = User.objects.get(email=form.cleaned_data["invitor"])
        except User.DoesNotExist:
            raise Exception("Can not find invitor")
        new_invitation = Invitation(user=invitor_obj, email=form.cleaned_data["email"], date_invited=datetime.now())
        new_invitation.save()
        return super(RegistrationViewInvite, self).register(form)
