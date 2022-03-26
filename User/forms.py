import email
from pyexpat import model
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.utils.translation import  ugettext as _

from .models import User, Student


# class UserRegisterForm(UserCreationForm):
#     """ Форма для регистрации """
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         if User.objects.filter(email__iexact=email).exists():
#             raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует")
#         return email

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control country'
            visible.field.widget.attrs['required'] = 'required'
            visible.field.widget.attrs['placeholder'] = visible.label


class StudentRegisterForm(BaseForm):
    """ Форма для регистрации студентов """
    email = forms.EmailField(label="Электронная почта")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())

    class Meta:
        model = Student
        exclude = ('account', 'parents',)
        # widgets = {
        #     'last_name': forms.CharField(attrs={'': 'Фамилия'}),
        # }


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
        self.user = None
        super().__init__(*args, **kwargs)

 
    def clean(self):
        email = self.cleaned_data.get('email').lower()
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user = User.objects.filter(email=email).get()
            if not self.user.is_active:
                raise ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
        return self.cleaned_data            

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login'
        )