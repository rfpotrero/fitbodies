from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product


@login_required
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


@login_required
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


@login_required
def update_review(request, review_id):
    """ 
    Update a user review
    """
    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.get(pk=review.product_id)
     
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review successfully updated!')
            return redirect(reverse('my_reviews'))
        else:
            messages.error(request, 'Review could not be update please review the comment area')
    else:
        form = ReviewForm(instance=review)

    template = 'reviews/update_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product from the store """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))