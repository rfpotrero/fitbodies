""" Admin file for contact """
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Dipslay class for the admin contact"""
    list_display = (
        'email',
        'contact_reason',
        'message',
    )


admin.site.register(Contact, ContactAdmin)
