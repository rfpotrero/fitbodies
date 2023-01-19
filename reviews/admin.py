""" Admin file for reviews """
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ Dipslay class for the admin contact"""
    list_display = (
        'user',
        'product',
        'comment',
        'create_at',
        'updated_at',
    )


admin.site.register(Review, ReviewAdmin)
