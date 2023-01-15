from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def personaltrainers(request):
    """ A view to return the Personal Trainers page """

    return render(request, 'home/index.html')


def classes(request):
    """ A view to return the clases """

    return render(request, 'home/index.html')