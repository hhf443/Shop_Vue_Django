from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from .filters import GoodsFilter
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer


class GoodsPagination(PageNumberPagination):
    page_size = 12
    # 灵活设置分页
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100




class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    # authentication_classes = (TokenAuthentication,)     # 局部验证
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
        List:
            商品分类列表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

# 使用ListAPIView
# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination


# class GoodsListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

# def post(self, request, format=None):
#     goods_serializer = GoodsSerializer(data=request.data)
#     if goods_serializer.is_valid():
#         goods_serializer.save()
#         return Response(goods_serializer.data, status=status.HTTP_201_CREATED)
#     return Response(goods_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
