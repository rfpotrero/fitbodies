""" Admin file for reviews """
from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'comment', 'created_at', 'updated_at')


admin.site.register(Review, ReviewAdmin)
