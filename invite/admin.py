from django.contrib import admin
from invite.models import Invitation
from django.forms import ModelForm

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = ['user', 'email', 'date_invited']

class InvitationAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'email', 'date_invited']
    list_display = ['user', 'email', 'date_invited']
    search_fields = ['user__name']
    form = InvitationForm

admin.site.register(Invitation, InvitationAdmin)    
