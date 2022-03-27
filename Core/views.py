from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View, TemplateView, FormView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'index.html'


@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response


class DashboardView(TemplateView):
    template_name = 'base/dashboard.html'





