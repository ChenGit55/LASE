from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Home(TemplateView):
    template_name = 'index.html'


class LionCubs(TemplateView):
    template_name = 'lion-cubs.html'


class Evolution(TemplateView):
    template_name = 'evolution.html'


class Lions(TemplateView):
    template_name = 'lions.html'
