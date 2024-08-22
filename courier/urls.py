from django.urls import path
from . import views

urlpatterns = [
    path('', views.courier_service, name='courier'),
    path('confirmation/', views.delivery_confirmation, name='delivery_confirmation'),
]