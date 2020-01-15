
from rest_framework import serializers
from .models import Goods, GoodsCategory

# 手动添加字段
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#
#     def create(self, validated_data):
#         return Goods.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        # fields = ('name', 'market_price', 'add_time', 'click_num')
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    # 显示外键的详细信息，实例化外键
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name', 'market_price', 'add_time', 'click_num')
        fields = '__all__'

