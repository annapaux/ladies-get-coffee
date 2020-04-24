# User Profile

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Company, University

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50, default='', blank=True)
    last_name = models.CharField(max_length = 50, default='', blank=True)
    email = models.CharField(max_length = 50, default='', blank=True, help_text="Provide an email peers can reach you at.")
    current_job = models.CharField(max_length = 50, default='', blank=True, help_text="Current job or status (e.g. software engineer, student, entrepreneur)")

    company = models.CharField(max_length = 50, blank=True, default='')
    university = models.CharField(max_length = 250, blank=True, default='')

    def __str__(self):
        return self.user
