from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import performance, channel, country, os
from .forms import performanceForm, channelForm, countryForm, osForm


class performanceListView(ListView):
    model = performance


class performanceCreateView(CreateView):
    model = performance
    form_class = performanceForm


class performanceDetailView(DetailView):
    model = performance


class performanceUpdateView(UpdateView):
    model = performance
    form_class = performanceForm


class channelListView(ListView):
    model = channel


class channelCreateView(CreateView):
    model = channel
    form_class = channelForm


class channelDetailView(DetailView):
    model = channel


class channelUpdateView(UpdateView):
    model = channel
    form_class = channelForm


class countryListView(ListView):
    model = country


class countryCreateView(CreateView):
    model = country
    form_class = countryForm


class countryDetailView(DetailView):
    model = country


class countryUpdateView(UpdateView):
    model = country
    form_class = countryForm


class osListView(ListView):
    model = os


class osCreateView(CreateView):
    model = os
    form_class = osForm


class osDetailView(DetailView):
    model = os


class osUpdateView(UpdateView):
    model = os
    form_class = osForm

