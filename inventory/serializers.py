from rest_framework import serializers
from .models import Inventory, InventoryHistory

class InventorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Inventory
        fields = '__all__'

class InventoryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryHistory
        fields = '__all__'