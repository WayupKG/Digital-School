from webbrowser import get
from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, FormView
from django.http import JsonResponse
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, ParentForm, StudentRegisterForm, AuthenticationForm
from .models import Student, Parent


class SignIn(TemplateView):
    """ Авторизация """
    template_name = 'signin.html'


class SignUpStudent(View):
    """ Регистрация студента """
    template_name = 'signup.html'

    def get(self, request, **kwargs):
        context = {}
        context["form"] = StudentRegisterForm()
        context["form_user"] = UserRegisterForm()
        context["parent_form"] = ParentForm()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        context["form"] = form = StudentRegisterForm(request.POST, request.FILES)
        context["form_user"] = form_user = UserRegisterForm(request.POST)
        context["parent_form"] = parent_form = ParentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            if form_user.is_valid():
                user = form_user.save(commit=False)
                user.last_name = student.last_name
                user.first_name = student.first_name
                if parent_form.is_valid():
                    parent = parent_form.save(commit=False)
                    student.account = user
                    student.parent = parent
                    parent.save()
                    user.save()
                    student.save()

        return render(self.request, self.template_name, context)


class AuthenticationValidator(View):
    """ Валидатор аутентификации """

    def post(self, *args, **kwargs) -> JsonResponse:
        form, context = AuthenticationForm(None, self.request.POST), {'success': False}
        if form.is_valid():
            login(self.request, form.get_user())
            context['success'] = True
        else:
            context['errors'] = form.errors
        return JsonResponse(context)


def sys_logout(request):
    """Выход"""
    logout(request)
    return redirect('sign_in')
