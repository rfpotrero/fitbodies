from django.shortcuts import render

from .models import Review

def add_review(request):

    template = 'reviews/add_review.html'
    context = {

    }
    return render(request, template, context)