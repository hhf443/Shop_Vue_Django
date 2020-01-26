from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
from trade.models import ShoppingCart
from trade.serializers import ShopCartSerializer, ShopCartDetailSerializer
from utils.permissions import IsOwnerOrReadOnly


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车功能
        list:
            获取购物车详情
        create:
            加入购物车
        delete:
            删除购物记录
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ShopCartSerializer
    lookup_field = 'goods_id'

    def get_serializer_class(self):
        if self.action=='list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)

