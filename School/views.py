from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View, TemplateView, FormView, ListView, DetailView


class DashboardRibbonView(TemplateView):
    template_name = 'dashboard/ribbon.html'