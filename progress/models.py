from django.db import models
from django.contrib.auth.models import User


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.CharField(max_length=3, null=True, blank=True)
    weight = models.CharField(max_length=3, null=True, blank=True)
    weight_goal = models.CharField(max_length=3, null=True, blank=True)
    chest = models.CharField(max_length=3, null=True, blank=True)
    waist = models.CharField(max_length=3, null=True, blank=True)

    def __st__(self):
        return self.user.first_name