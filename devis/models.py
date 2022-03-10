from io import BytesIO
from unittest.mock import DEFAULT
from django.db import models



class Devi(models.Model):
    # Infos person
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # Info company
    siret = models.CharField(max_length=14, blank=True, null=True)
    raison_sociale = models.CharField(max_length=255, blank=True, null=True)
    # Info message
    object = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    status = models.IntegerField(default=0)
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name
