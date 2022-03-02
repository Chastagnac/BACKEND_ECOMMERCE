
from rest_framework import serializers

from .models import Devi

class DevisSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Devi 
        fields = (
            "id",
            "name", 
            "email",
            "siret",
            "raison_sociale",
            "object",
            "category",
            "content",
            "status"
        ) 

class DevisSet(serializers.ModelSerializer):
    class Meta: 
        model = Devi 
        fields = ('status',) 