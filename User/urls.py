from django.urls import path
from .views import SignIn, SignUpStudent, AuthenticationValidator, sys_logout

urlpatterns = [
    path('sign-in/', SignIn.as_view(), name='sign_in'),
    path('sign-up-student/', SignUpStudent.as_view(), name='sign_up_student'),
    path('logout/', sys_logout, name='logout'),
    path('auth-validator/', AuthenticationValidator.as_view(), name='auth_v')
]