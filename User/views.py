from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView, FormView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, ParentForm, StudentRegisterForm, AuthenticationForm
from .models import Student, Parent
from .mixins import AdminRequiredMixin


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
                    return redirect('successfully')
        return render(self.request, self.template_name, context)


class SignUpSuccessfully(TemplateView):
    """Страница Успеха"""
    template_name = 'successfully.html'
    

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


class ActiveStudentView(AdminRequiredMixin, View):
    """Активировать аккаунт ученика"""
    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.select_related('account', 'school').get(pk=pk)
        if student.school.admin != request.user:
            return self.handle_no_permission()
        student.account.is_active = True
        student.account.save()
        return redirect('ribbon')
    

class InActiveStudentView(AdminRequiredMixin, View):
    """Деактивировать аккаунт ученика"""
    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.select_related('account', 'school').get(pk=pk)
        if student.school.admin != request.user:
            return self.handle_no_permission()
        student.account.is_active = False
        student.account.save()
        return redirect('ribbon')


class RemoveStudentView(AdminRequiredMixin, View):
    """Удаление аккаунт ученика"""
    def get(self, request, pk, *args, **kwargs):
        student = Student.objects.select_related('account', 'school').get(pk=pk)
        if student.school.admin != request.user:
            return self.handle_no_permission()
        user = student.account
        student.parent.delete()
        student.delete()
        user.delete()
        return redirect('ribbon')


def sys_logout(request):
    """Выход"""
    logout(request)
    return redirect('sign_in')
