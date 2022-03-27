from django.urls import path

from . import views

urlpatterns = (
    path('dashboard/ribbon/', views.DashboardRibbonView.as_view(), name='ribbon'),
)