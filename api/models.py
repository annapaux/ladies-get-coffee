from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 50, null=False, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/api/company/%i/" % self.id

class University(models.Model):
    name = models.CharField(max_length = 250, null=False, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/api/university/%i/" % self.id
