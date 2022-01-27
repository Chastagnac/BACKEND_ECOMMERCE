
from rest_framework import serializers

from .models import Devi

class DevisSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Devi 
        fields = (
            "id",
            "status",
            "name", 
            "email",
            "siret",
            "raison_sociale",
            "object",
            "category",
            "content",
        ) 