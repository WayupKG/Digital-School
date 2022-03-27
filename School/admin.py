from django.contrib import admin
from .models import School, AcademicClass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'training_base', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('title',)


@admin.register(AcademicClass)
class AcademicClassAdmin(admin.ModelAdmin):
    list_display = ('edu_grade', 'name_class', 'shift', 'capacity', 'language')
    list_filter = ('edu_grade', 'shift', 'language')
    search_fields = ('title',)
