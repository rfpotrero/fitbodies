from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.add_contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
]