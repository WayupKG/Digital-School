from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.SignIn.as_view(), name='sign_in'),
    path('sign-up-student/', views.SignUpStudent.as_view(), name='sign_up_student'),
    path('successfully/', views.SignUpSuccessfully.as_view(), name='successfully'),
    path('logout/', views.sys_logout, name='logout'),
    path('auth-validator/', views.AuthenticationValidator.as_view(), name='auth_v'),
    path('active/<int:pk>/', views.ActiveStudentView.as_view(), name='active_student'),
    path('inactive/<int:pk>/', views.InActiveStudentView.as_view(), name='inactive_student'),
    path('remove/<int:pk>/', views.RemoveStudentView.as_view(), name='remove_student'),
]