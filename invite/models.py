from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from registration.forms import RegistrationFormUniqueEmail
from django import forms

class Invitation(models.Model):
    user = models.ForeignKey(User, verbose_name='Invitor',
                             related_name='invitations', on_delete=models.SET_NULL, null=True)
    email = models.EmailField(verbose_name="Email")
    date_invited = models.DateTimeField(default=datetime.now,
                                        verbose_name='date invited')

class MyRegistrationForm(RegistrationFormUniqueEmail):
    MAX_INVITATIONS = 1
    
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'name': "password1",
                                                                                            'type': "password"}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'name': "password2",
                                                                                            'type': "password"}))
    invitor = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


    error_messages = {
        'invalid_invitor': 'Can not find invitor in laicode database',
        'no_more_invitation': 'No more invitations from this invitor',
    }

    def clean_invitor(self):
        invitor = self.cleaned_data["invitor"]

        try:
            invitor_obj = User.objects.get(email=invitor)
        except User.DoesNotExist:
            raise forms.ValidationError(
                self.error_messages['invalid_invitor'],  #user my customized error message
                code='invalid_invitor',   #set the error message key
            )

        try:
            invitations = Invitation.objects.get(user_id=invitor_obj.id).count()
            if invitations >= INVITATIONS: 
                raise forms.ValidationError(
                    self.error_messages['no_more_invitation'],
                    code='no_more_invitation',
                )
        except Invitation.DoesNotExist:
            pass
            
        return invitor
