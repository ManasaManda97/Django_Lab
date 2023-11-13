from django.urls import path
from . import views

urlpatterns = [
    path('AppTwo/', views.AppTwo, name='AppTwo'),
]
