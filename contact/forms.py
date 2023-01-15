from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Model to capture users contact
    """

    class Meta:
        model = Contact
        fields = ['name',
                  'email',
                  'message',
                  'contact_reason']
