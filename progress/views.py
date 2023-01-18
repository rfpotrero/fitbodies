from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProgress
from .forms import UserProgressForm

@login_required
def view_progress(request):
    """
    View to display current user progress
    """
    form = UserProgressForm()

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
                user_progress.save()  # Update the exisitng info.
                kilos_to_go = int(user_progress.weight_goal) - int(user_progress.weight)
                messages.success(request, 'Profile updated successfully')
            except UserProgress.DoesNotExist:
                # create a new UserProgress object if none exists
                user_progress = UserProgress(user=request.user,
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                weight_goal=form.cleaned_data['weight_goal'],
                chest=form.cleaned_data['chest'],
                waist=form.cleaned_data['waist'])
                user_progress.save()
                if user_progress.weight_goal and user_progress.weight:
                    kilos_to_go = int(user_progress.weight_goal) - int(user_progress.weight)
                else:
                    kilos_to_go = None
                messages.success(request, 'Profile updated successfully')

            template = 'progress/progress.html'
            context = {
                'form': form,
                'user_progress': user_progress,
                'kilos_to_go': kilos_to_go
            }

            return render(request, template, context)
    
    try:
        user_progress = UserProgress.objects.get(user=request.user)
        form = UserProgressForm(instance=user_progress)
        if user_progress.weight_goal and user_progress.weight:
            kilos_to_go = int(user_progress.weight_goal) - int(user_progress.weight)
        else:
            kilos_to_go = None
        context = {
            'form': form,
            'user_progress': user_progress,
            'kilos_to_go': kilos_to_go
                }
        template = 'progress/progress.html'
        return render(request, template, context)
        
    except UserProgress.DoesNotExist:
        #if request method is GET AND no UserProgress display the empty form
        form = UserProgressForm()
    context = {
        'form': form,
        'kilos_to_go': kilos_to_go
    }
    template = 'progress/progress.html'
    return render(request, template, context)
