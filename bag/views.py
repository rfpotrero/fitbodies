from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    product = Product.objects.get(pk=item_id)

    if item_id in list(bag.keys()):
        messages.error(request, "The item is already in the cart")
    else:
        bag[item_id] = 1
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from cart')

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)