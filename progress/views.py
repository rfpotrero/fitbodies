from django.shortcuts import render
from .models import UserProgress

from .forms import UserProgressForm


def view_progress(request):


    if request.method == 'POST':
        form = UserProgressForm(request.POST)
        if form.is_valid():
        # check if user already has a UserProgress object
            try:
                user_progress = UserProgress.objects.get(user=request.user)
                # update the existing object with form data
                user_progress.height = form.cleaned_data['height']
                user_progress.weight = form.cleaned_data['weight']
                user_progress.weight_goal = form.cleaned_data['weight_goal']
                user_progress.chest = form.cleaned_data['chest']
                user_progress.waist = form.cleaned_data['waist']
                user_progress.save() # Update the exisitng info.
            except UserProgress.DoesNotExist:
                # create a new UserProgress object if none exists
                user_progress = UserProgress(user=request.user,
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                weight_goal=form.cleaned_data['weight_goal'],
                chest=form.cleaned_data['chest'],
                waist=form.cleaned_data['waist'])
                user_progress.save()

            template = 'progress/progress.html'
            context = {
                'form': form,
            }

            return render(request, template, context)
        
    # if request method is GET display the form
    form = UserProgressForm()
    context = {
        'form': form,
        'user_progress':user_progress
    }
    template = 'progress/progress.html'
    return render(request, template, context)

