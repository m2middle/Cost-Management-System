from django.shortcuts import render
from rest_framework import generics
from .models import Inventory, InventoryHistory
from .serializers import InventorySerializer, InventoryHistorySerializer

# Create your views here.

class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class InventoryHistoryListCreate(generics.ListCreateAPIView):
    queryset = InventoryHistory.objects.all()
    serializer_class = InventoryHistorySerializer

class InventoryHistoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryHistory.objects.all()
    serializer_class = InventoryHistorySerializer