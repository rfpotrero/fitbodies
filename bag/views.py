from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, "The item is already in the cart")
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)