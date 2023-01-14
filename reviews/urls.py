from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<product_id>/', views.add_review, name='add_review'),
    path('reviews/<product_id>/', views.view_reviews, name='view_reviews'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('update_review/<review_id>/', views.update_review, name='update_review'),
    path('delete/<review_id>/', views.delete_review, name='delete_review'),
]