from django.contrib.auth.hashers import make_password, check_password
from django.contrib import admin

from .models import User, Student


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'email', 'status', 'is_superuser', 'is_staff', 'is_active', 'created_at', 'updated_at')
    list_filter = ('status', 'is_superuser', 'is_active')
    
    def save_model(self, request, obj, form, change):
        user = User.objects.get(pk=obj.pk)
        # Сначала проверьте случай, когда пароль не закодирован, а затем проверьте, если пароль закодирован.
        if not (check_password(form.data['password'], user.password) or user.password == form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user.password
        super().save_model(request, obj, form, change)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'account', 'gender', 'school', 'edu_grade', 'created_at', 'updated_at')
    list_filter = ('school', 'edu_grade', 'gender')