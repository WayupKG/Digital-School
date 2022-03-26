from django.shortcuts import redirect
from django.views.generic import View, TemplateView, FormView
from django.http import JsonResponse
from django.contrib.auth import login, logout

from .forms import StudentRegisterForm, AuthenticationForm
from .models import Student


class SignIn(TemplateView):
    """ Авторизация """
    template_name = 'signin.html'


class SignUpStudent(FormView):
    """ Регистрация студента """
    form_class = StudentRegisterForm
    template_name = 'signup.html'


class AuthenticationValidator(View):
    """ Валидатор аутентификации """
    def post(self, *args, **kwargs) -> JsonResponse:
        form, context = AuthenticationForm(None, self.request.POST), {'success': False}
        if form.is_valid():
            login(self.request, form.get_user())
            context['success'] = True
        else: context['errors'] = form.errors
        return JsonResponse(context)


def sys_logout(request):
    """Выход"""
    logout(request)
    return redirect('sign_in')