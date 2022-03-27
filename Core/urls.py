from django.urls import path

from . import views

urlpatterns = (
    path('', views.IndexView.as_view(), name='index'),
    path('csrf-token/', views.get_csrf, name='get_csrf'),
)