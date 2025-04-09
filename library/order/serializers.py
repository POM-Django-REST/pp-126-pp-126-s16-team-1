from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at']