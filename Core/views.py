from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


