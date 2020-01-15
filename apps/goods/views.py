from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializers import GoodsSerializer

class GoodsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request, format=None):
        goods_serializer = GoodsSerializer(data=request.data)
        if goods_serializer.is_valid():
            goods_serializer.save()
            return Response(goods_serializer.data, status=status.HTTP_201_CREATED)
        return Response(goods_serializer.errors, status=status.HTTP_400_BAD_REQUEST)