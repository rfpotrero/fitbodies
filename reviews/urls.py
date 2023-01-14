from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<product_id>/', views.add_review, name='add_review'),
    path('reviews/<product_id>/', views.view_reviews, name='view_reviews'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
]