from django.shortcuts import render, redirect, get_object_or_404

from .models import Review
from .forms import ReviewForm
from products.models import Product


def add_review(request, product_id):
    """
    View to add review to product.
    """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()

            return redirect('product_detail', product_id=product.pk)

    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product
    }
    return render(request, template, context)


def view_reviews(request, product_id):
    """
    View to display all reviews for a specific product
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product_id=product.pk)

    template = 'reviews/view_reviews.html'
    context = {
        'reviews': reviews,
        'product': product,
        }
    return render(request, template, context)


def my_reviews(request):
    """
    View to display all user's reviews 
    """

    reviews = Review.objects.filter(user=request.user)

    template = 'reviews/my_reviews.html'
    context = {
        'reviews': reviews
    }

    return render(request, template, context)