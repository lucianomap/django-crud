from django.db import models


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=200)
    entry_day = models.CharField()
    exit_day = models.CharField(null=True, blank=True)
