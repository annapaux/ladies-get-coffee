# User Profile

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50, default='', blank=True)
    last_name = models.CharField(max_length = 50, default='', blank=True)
    email = models.CharField(max_length = 50, default='', blank=True)
    current_job = models.CharField(max_length = 50, default='', blank=True)

    def __str__(self):
        return self.user

class Company(models.Model):
    name = models.CharField(max_length = 50, null=False, db_index=True)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length = 250, null=False, db_index=True)

    def __str__(self):
        return self.name
