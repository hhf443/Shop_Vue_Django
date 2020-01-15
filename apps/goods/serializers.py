
from rest_framework import serializers
from .models import Goods
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)

    def create(self, validated_data):
        return Goods.objects.create(**validated_data)
