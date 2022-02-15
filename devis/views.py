from django.http import Http404, JsonResponse
from django.db.models import Q
from django.views import View
from rest_framework import serializers, status

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

    def post(self, request, *args, **kwargs):
        serializer = DevisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
