from rest_framework import serializers
from inventory.models import InventoryRegistration

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryRegistration
        fields='__all__'