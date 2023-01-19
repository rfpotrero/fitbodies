from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form used to capture logged user reviews.
    """

    class Meta:
        model = Review
        fields = ['comment']
