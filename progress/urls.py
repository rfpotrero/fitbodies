from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_progress, name='progress'),
]
