from django.shortcuts import render
from api_1.models import Women
from rest_framework import generics
from api_1.serializer import WomenSerializer

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer