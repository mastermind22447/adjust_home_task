from django import forms
from .models import performance, channel, country, os


class performanceForm(forms.ModelForm):
    class Meta:
        model = performance
        fields = ['name', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'id', 'os', 'country', 'channel']


class channelForm(forms.ModelForm):
    class Meta:
        model = channel
        fields = ['name']


class countryForm(forms.ModelForm):
    class Meta:
        model = country
        fields = ['name']


class osForm(forms.ModelForm):
    class Meta:
        model = os
        fields = ['name']
