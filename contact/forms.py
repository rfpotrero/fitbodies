""" Forms for Contact us form """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Model to capture users contact
    """

    class Meta:
        """ Forms fields """
        model = Contact
        fields = ['name',
                  'email',
                  'message',
                  'contact_reason']
