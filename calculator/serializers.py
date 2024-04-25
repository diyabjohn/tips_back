from rest_framework import serializers
from .models import Tip

class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ['id', 'bill_amount', 'tip_percentage', 'total_tip', 'total_amount', 'created_at']

