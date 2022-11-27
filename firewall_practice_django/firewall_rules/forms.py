from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm

from .models import firewall_rules

class get_firewall_rules(ModelForm):
    class Meta:
        model = firewall_rules
        fields = [
            'zone',
            'direction',
            'source_ip',
            'source_protocol',
            'source_detail',
            'destination_ip',
            'destination_protocol',
            'destination_detail',
            'action',
            'description']

class register_form(ModelForm):
    class Meta:
        model = User
        fields = ("username","password")
        
    def save(self, commit=True):
        user = super(register_form, self).save(commit=False)
        if commit:
            user.save()
        return user