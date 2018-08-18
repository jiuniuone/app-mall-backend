import json

from mall.models import Address, Member, Order, OrderItem, PropertyItem
from mall.views.api import ApiView, api_route


class Resource(ApiView):

    # http "localhost/api/mall/order/create?token=kQkJvnrXmCOlR%2B482qnLOw%3D%3D&productJsonStr=%5B%7B%22product_id%22%3A17233%2C%22count%22%3A1%2C%22items%22%3A%22299%3A1226%2C%22%2C%22logisticsType%22%3A0%2C%20%22inviter_id%22%3A0%7D%2C%7B%22product_id%22%3A17233%2C%22count%22%3A5%2C%22items%22%3A%22299%3A1225%2C%22%2C%22logisticsType%22%3A0%2C%20%22inviter_id%22%3A0%7D%5D&remark=&addressId=4"
    @api_route('/order/create')
    def create(self):
        token, productJsonStr, remark = self.param(["token", "productJsonStr", "remark"])
        address_id = self.int_param("addressId")
        print(token, productJsonStr, remark, address_id)
        if token and productJsonStr and address_id:
            print(token)
            member = Member.objects.filter(token=token).first()
            address = Address.objects.filter(id=address_id).first()
            if member and address:
                item_array = []
                for obj in json.loads(productJsonStr):
                    amount = obj.pop("count", 0)
                    items = obj.pop("items", None)
                    if amount and items:
                        item_id = int(items.split(",")[0].split(":")[1])
                        item: PropertyItem = PropertyItem.objects.filter(id=item_id).first()
                        if item:
                            item_array.append((item, amount))

                count = 0
                fee = 0
                if item_array:
                    order: Order = Order.objects.create(address=address)
                    for (item, amount) in item_array:
                        OrderItem.objects.create(order=order, item=item, amount=amount)
                        count += amount
                        fee += amount * item.price

                    return self.json_response({
                        "code": 0,
                        "data": {
                            "amountLogistics": 1,
                            "score": member.score,
                            "goodsNumber": count,
                            "free_shipping_for_purchases": 1,
                            "isNeedLogistics": True,
                            "amountTotle": fee

                        }
                    })
        return self.json_response({"code": 1})

    # http "https://api.it120.cc/tianguoguoxiaopu/order/statistics?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/order/statistics')
    def statistics(self):
        return self.json_response({
            "code": 0,
            "data": {
                "count_id_no_reputation": 0,
                "count_id_no_transfer": 0,
                "count_id_close": 0,
                "count_id_no_pay": 1,
                "count_id_no_confirm": 0,
                "count_id_success": 0
            },
            "msg": "success"
        })

    # http "https://api.it120.cc/tianguoguoxiaopu/order/list?token=c6d64df6-50b6-4012-a7e5-868749fe383a&pageSize=10000&page=1"
    @api_route('/order/list')
    def list(self):
        return self.file_json_response("/order/list.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/order/close?token=c6d64df6-50b6-4012-a7e5-868749fe383a&orderId=133059"
    @api_route('/order/close')
    def close(self):
        return self.json_response({"code": 0, "msg": "success"})

    # http "https://api.it120.cc/tianguoguoxiaopu/order/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=133068"
    @api_route('/order/detail')
    def detail(self):
        return self.file_json_response("/order/detail.json")
