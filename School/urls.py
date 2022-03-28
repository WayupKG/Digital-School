from django.urls import path

from .import views

urlpatterns = (
    path('dashboard/ribbon/', views.DashboardRibbonView.as_view(), name='ribbon'),
    path('dashboard/student/management/', views.ManagementStudentView.as_view(), name='management'),
    path('dashboard/student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),
    path('dashboard/student/<int:pk>/detail/', views.StudentDetailView.as_view(), name='student_detail'),
)