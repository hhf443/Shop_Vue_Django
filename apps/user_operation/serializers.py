from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from goods.serializers import GoodsSerializer
from .models import UserFav, UserLeavingMessage


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(queryset=UserFav.objects.all(), fields=('user', 'goods'), message='已经收藏')
        ]
        fields = ('user', 'goods', 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UserLeavingMessage
        fields = ('id', 'user', 'message_type', 'subject', 'message', 'file', 'add_time')


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserLeavingMessage
        fields = ('id', 'user', 'message_type', 'subject', 'message', 'file', 'add_time')