from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('classes/', views.classes, name='classes'),
]