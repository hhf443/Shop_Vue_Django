"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet
# from goods.views import GoodsListView
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from users.views import SmsCodeViewSet, UserViewSet
from trade.views import ShoppingCartViewSet

router = DefaultRouter()
# 配置goods的url
router.register('goods', GoodsListViewSet, basename='goods')
# 配置category的url
router.register('categorys', CategoryViewSet, basename='categorys')
# 配置验证码注册
router.register('codes', SmsCodeViewSet, basename='codes')
# 配置验证码注册
router.register('users', UserViewSet, basename='users')
# 收藏功能
router.register('userfavs', UserFavViewSet, basename='userfavs')
# 留言
router.register('messages', LeavingMessageViewSet, basename='messages')
# 收货地址
router.register('address', AddressViewSet, basename='address')
# 购物车url
router.register('shopcarts', ShoppingCartViewSet, basename='shopcarts')

urlpatterns = [
       # path('media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
       # path('goods/', GoodsListView.as_view(), name='goods-list'),
       # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
       path('xadmin/', xadmin.site.urls),

       re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

       path('', include(router.urls)),

       path('docs/', include_docs_urls(title='生鲜电商')),

       path('api-token-auth/', views.obtain_auth_token),
       path('login/', obtain_jwt_token)
]
