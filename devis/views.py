from django.http import Http404
from django.db.models import Q
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Devi
from .serializers import DevisSerializer



class LatestQuoteList(APIView):
    def get(self, request, format=None):
        devis = Devi.objects.all()
        serializer = DevisSerializer(devis, many=True)
        return Response(serializer.data)