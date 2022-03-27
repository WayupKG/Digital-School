from dataclasses import fields
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.translation import  ugettext as _

from .models import User, Parent, Student


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'required'
            visible.field.widget.attrs['placeholder'] = visible.label
            

class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации аккаунта """
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует")
        return email
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = 'required'
            visible.field.widget.attrs['placeholder'] = visible.label


class ParentForm(BaseForm):
    """ Форма для регистрации родителей """
    class Meta:
        model = Parent
        fields = '__all__'


class StudentRegisterForm(BaseForm):
    """ Форма для регистрации студентов """
    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'sur_name',
                  'gender', 'date_birth', 'address', 'phone', 'school', 'edu_grade', 'image']


class AuthenticationForm(forms.Form):
    """Форма для авторизации"""
    email = forms.EmailField()
    password = forms.CharField()

    error_messages = {
        'invalid_login': _(
            "Пожалуйста, введите правильный адрес электронной почты и пароль. Обратите внимание, что пароль чувствителен к регистру."
        ),
        'inactive': _("Ваша учетная запись находится на рассмотрении."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        Параметр «запрос» установлен для пользовательского использования аутентификации подклассами.
        Данные формы поступают через стандартный kwarg «data».
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email').lower()
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                self.get_invalid_login_error('invalid_login')
            elif not self.user_cache.is_active:
                self.get_invalid_login_error('inactive')
        return self.cleaned_data            

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self, error):
        raise ValidationError(
            self.error_messages[error],
            code=error,
        )