from django.shortcuts import render
from rest_framework import viewsets, routers
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


