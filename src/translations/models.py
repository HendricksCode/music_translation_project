from django.db import models

# Create your models here.
class Translate(models.Model):
    english     = models.CharField(max_length=120)
    italian     = models.CharField(max_length=120, blank=True, null=True)
    german      = models.CharField(max_length=120, blank=True, null=True)
    french      = models.CharField(max_length=120, blank=True, null=True)
    