from io import BytesIO
from django.db import models



class Statu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'



class Devi(models.Model):
    status = models.ForeignKey(
    Statu, related_name='devis', on_delete=models.CASCADE)
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

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
