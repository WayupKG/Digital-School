from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext as _

from Core.services import get_translit
from .managers import UserManager


def upload_to_image(instance, filename):
    list_file = filename.split('.')
    return f"avatars/{instance.pk}-{instance.get_name_translit()}/{instance.get_name_translit()}.{list_file[-1]}/"


class User(AbstractBaseUser, PermissionsMixin):
    """Пользователь"""
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    STATUS = (
        ("admin", "Администратор"),
        ("teacher", "Преподаватель"),
        ("student", "Студент")
    )

    last_name = models.CharField(_('Фамилия'), max_length=40)
    first_name = models.CharField(_('Имя'), max_length=40)
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(_('Пароль'), max_length=255,
                                help_text=_("Вы можете изменить пароль, написав в это поле"))
    status = models.CharField(_("Статус"), max_length=20, choices=STATUS, default="student")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["last_name", "first_name"]

    def get_full_name(self):
        '''Возвращает first_name, last_name с пробелом между ними.'''
        return f"{self.first_name} {self.last_name}"

    def get_name_translit(self):
        return get_translit(f'{self.last_name} {self.first_name}')

    def get_short_name(self):
        '''Возвращает сокращенное имя пользователя.'''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''Отправляет электронное письмо этому пользователю.'''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Parent(models.Model):
    """Родитель (Отец, Мать)"""
    class Meta:
        verbose_name = _('Родитель')
        verbose_name_plural = _('Родители')

    father_last_name = models.CharField(_('Фамилия'), max_length=40)
    father_first_name = models.CharField(_('Имя'), max_length=40)
    father_sur_name = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    father_phone = models.CharField(_("Номер телефона"), max_length=15)
    father_job = models.CharField(_("Работа"), max_length=255)

    mother_last_name = models.CharField(_('Фамилия'), max_length=40)
    mother_first_name = models.CharField(_('Имя'), max_length=40)
    mother_sur_name = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    mother_phone = models.CharField(_("Номер телефона"), max_length=15)
    mother_job = models.CharField(_("Работа"), max_length=255)

    def __str__(self) -> str:
        return f"{self.father_first_name} {self.mother_first_name}"

    def get_father_full_name(self):
        if self.father_sur_name:
            return f"{self.father_last_name} {self.father_first_name} {self.father_sur_name}"
        return f"{self.father_last_name} {self.father_first_name}"
    
    def get_mother_full_name(self):
        if self.mother_sur_name:
            return f"{self.mother_last_name} {self.mother_first_name} {self.mother_sur_name}"
        return f"{self.mother_last_name} {self.mother_first_name}"


class Student(models.Model):
    """Ученик"""
    class Meta:
        verbose_name = _('Ученик')
        verbose_name_plural = _('Ученики')

    GENDER = (
        (None, 'Выберите пол'),
        ('man', 'Мужчина'),
        ('woman', 'Женщина')
    )

    last_name = models.CharField(_('Фамилия'), max_length=40)
    first_name = models.CharField(_('Имя'), max_length=40)
    sur_name = models.CharField(_('Отчество'), max_length=50, blank=True, null=True)
    account = models.OneToOneField(User, verbose_name=_("Аккаунт"), on_delete=models.PROTECT)
    gender = models.CharField(_("Пол"), max_length=10, choices=GENDER)
    date_birth = models.DateField(_("Дата рождения"))
    address = models.CharField(_("Адрес"), max_length=255)
    phone = models.CharField(_("Номер телефона"), max_length=15)
    school = models.ForeignKey('School.School', verbose_name=_("Школа"),
                               on_delete=models.PROTECT, related_name="students")
    edu_grade = models.ForeignKey('School.AcademicClass', verbose_name=_("Академический класс"), on_delete=models.PROTECT)
    image = models.ImageField(verbose_name=_("Фотография"), upload_to=upload_to_image, null=True, blank=True)
    parent = models.ForeignKey(Parent, verbose_name=_("Родители"), on_delete=models.CASCADE, related_name="students")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_full_name(self):
        '''Возвращает first_name, last_name и sur_name с пробелом между ними.'''
        if self.sur_name:
            return f"{self.first_name} {self.last_name} {self.sur_name}"
        return f"{self.first_name} {self.last_name}"

    def get_name_translit(self):
        return get_translit(self.get_full_name())

    def get_short_name(self):
        '''Возвращает сокращенное имя пользователя.'''
        return self.first_name