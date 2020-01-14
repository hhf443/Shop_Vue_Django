
from django.views.generic.base import View
from goods.models import Goods

class GoodsListView(View):
    def get(selfself, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        # 由于datatime格式无法传递，故用这种方法会出错
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append((json_dict))

        # 这种不需要一个个手动提取字段，但imagefieldfile仍会出错
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(goods)
        #     json_list.append(json_dict)
        # from django.http import HttpResponse
        # import json
        # # 注意dumps,+s
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        from django.core import serializers
        from django.http import HttpResponse, JsonResponse
        import json
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)  # 和json.dumps是相反的操作
        # # 注意dumps,+s
        # return HttpResponse(json.dumps(json_data), content_type='application/json')
        return JsonResponse(json_data, safe=False)

