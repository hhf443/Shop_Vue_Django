import sys
import os

# 独立使用model
pwd = os.path.dirname(os.path.realpath(__file__))   # 获得当前目录
sys.path.append(pwd+"../")  # 当前目录加入python搜索路径之下

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MxShop.settings')
import django
django.setup()

from goods.models import GoodsCategory, Goods, GoodsImage
from db_tools.data.product_data import row_data


for goods_detial in row_data:
    goods = Goods()
    goods.name = goods_detial["name"]
    goods.market_price = float(int(goods_detial["market_price"].replace("￥", "").replace("元", "")))
    goods.shop_price = float(int(goods_detial["market_price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = goods_detial["desc"] if goods_detial["desc"] is not None else ""
    goods.goods_desc = goods_detial["goods_desc"] if goods_detial["goods_desc"] is not None else ""
    goods.goods_front_image = goods_detial["images"][0] if goods_detial["images"] is not None else ""

    category_name = goods_detial["categorys"][-1]
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detial["images"]:
        goods_image_intance = GoodsImage()
        goods_image_intance.image = goods_image
        goods_image_intance.goods = goods
        goods_image_intance.save()