from django.shortcuts import render
from .models import UserProgress

def view_progress(request):

    template = 'progress/progress.html'
    context = {
      
    }
    return render(request, template, context)
