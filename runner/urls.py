from django.urls import path
from . import views

urlpatterns = [
    path('', views.runner_service, name='runner'),
    path('confirmation/', views.errand_confirmation, name='errand_confirmation'),
]