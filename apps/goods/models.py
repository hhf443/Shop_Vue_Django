from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class GoodsCategory(models.Model):

    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.CharField(default="", verbose_name="类别描述", help_text="类别描述")   # 简单描述
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别",
                                        help_text="父类目级别", related_name="sub_cat")
    # 父级，需要指向自己 | blank不允许为空，但允许null作为其中一个选项
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")     # 默认为false
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    '''
    品牌名
    '''
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌类别")
    desc = models.CharField(default="", verbose_name="品牌描述", help_text="品牌描述")   # 简单描述
    image = models.ImageField(max_length=200, upload_to="brand/images/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Goods(models.Model):
    '''
    商品
    '''
    category = models.ForeignKey(GoodsCategory)
    goods_sn = models.CharField()
    name = models.CharField()
    click_num = models.IntegerField()
    sold_num = models.IntegerField()
    fav_num = models.IntegerField()
    goods_num = models.IntegerField()
    market_price = models.FloatField()
    shop_price = models.FloatField()
    goods_brief = models.TextField()
    goods_desc = UEditorField()
    ship_free = models.BooleanField()