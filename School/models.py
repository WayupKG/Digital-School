from django.utils.translation import ugettext_lazy as _
from django.db import models


class School(models.Model):
    """Школа"""

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Школа')
        verbose_name_plural = _('Школы')

    CLASS = (
        ('9-class', 'Неполное среднее общее образование'),
        ('11-class', 'Среднее общее образование'),
    )

    title = models.CharField(_("Называние"), max_length=255, unique=True, db_index=True)
    number = models.PositiveSmallIntegerField(_("Номер"), default=0)
    training_base = models.CharField(_("Учебный база"), max_length=20, choices=CLASS, default='11-class')
    is_active = models.BooleanField(_('Активный'), default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.number}"


class AcademicClass(models.Model):
    """Академический класс"""

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    LANGUAGE = (
        ('kg', 'Кыргызский язык'),
        ('ru', 'Русский язык'),
        ('kz', 'Казакский язык'),
        ('en', 'Англиский язык'),
    )

    EDU_GRADE = (
        ('1', 'Начального общего образования - 1'),
        ('2', 'Начального общего образования - 2'),
        ('3', 'Начального общего образования - 3'),
        ('4', 'Начального общего образования - 4'),
        ('5', 'Основного общего образования - 5'),
        ('6', 'Основного общего образования - 6'),
        ('7', 'Основного общего образования - 7'),
        ('8', 'Основного общего образования - 8'),
        ('9', 'Основного общего образования - 9'),
        ('10', 'Сердного общего образования - 10'),
        ('11', 'Сердного общего образования - 11'),
    )

    SHIFT = (
        ('one', 'Первая смена'),
        ('two', 'Втарая смена'),
    )

    edu_grade = models.CharField(_("Урвень образования"), max_length=50, choices=EDU_GRADE, default='1')
    language = models.CharField("Язык", max_length=50, choices=LANGUAGE, default='kg')
    shift = models.CharField(_("Смена"), max_length=15, choices=SHIFT, default='one')
    capacity = models.PositiveSmallIntegerField("Вместимость", default=0)
    name_class = models.CharField("Называние класса", max_length=5)

    def __str__(self) -> str:
        return str(self.name_class)
