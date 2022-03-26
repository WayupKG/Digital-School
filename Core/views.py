from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView, ListView, DetailView


class HomeView(View):

    def get(self, *args, **kwargs):
        return 'asd'



