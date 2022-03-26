from django.contrib import admin
from .models import User, Student


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'status', 'is_superuser', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('status', 'is_superuser', 'is_active')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('get_full_name', 'account', 'gender', 'school', 'edu_grade', 'created_at', 'updated_at')
    list_filter = ('school', 'edu_grade', 'gender')