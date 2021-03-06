import json
import random
from mall.models import Address, Member, Order, OrderItem, OrderLog, PropertyItem, Property, Product, OrderStatus, Reputation
from mall.views.api import ApiView, api_route


def create_order_number():
    while True:
        result = (random.randint(12345678901234567890, 99999999999999999999))
        if not Order.objects.filter(order_number=result).first():
            return result


class Resource(ApiView):

    # 余额付款
    @api_route('/order/pay/balance')
    def pay_with_balance(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        order: Order = Order.objects.filter(id=self.int_param("orderId")).first()
        if member and order:
            money = member.balance - order.fee
            if money > 0:
                member.balance -= money
                order.status = OrderStatus.to_deliver
                member.save()
                order.save()
                OrderLog.objects.create(order=order, status=OrderStatus.to_deliver)
                return self.ok()

        return self.error(code=1, message="error to pay")

    # http "localhost/api/mall/order/create?token=kQkJvnrXmCOlR%2B482qnLOw%3D%3D&productJsonStr=%5B%7B%22product_id%22%3A17233%2C%22count%22%3A1%2C%22items%22%3A%22299%3A1226%2C%22%2C%22logisticsType%22%3A0%2C%20%22inviter_id%22%3A0%7D%2C%7B%22product_id%22%3A17233%2C%22count%22%3A5%2C%22items%22%3A%22299%3A1225%2C%22%2C%22logisticsType%22%3A0%2C%20%22inviter_id%22%3A0%7D%5D&remark=&addressId=4"
    @api_route('/order/create')
    def create(self):
        token, productJsonStr, remark = self.param(["token", "productJsonStr", "remark"])
        address_id = self.int_param("addressId")
        if token and productJsonStr and address_id:
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
                    order: Order = Order.objects.create(
                        address=address,
                        status=OrderStatus.to_pay,
                        order_number=create_order_number(),
                        remark=remark
                    )
                    for (item, amount) in item_array:
                        OrderItem.objects.create(order=order, item=item, amount=amount)
                        count += amount
                        fee += amount * item.price
                    order.fee = fee
                    order.save()
                    OrderLog.objects.create(order=order, status=OrderStatus.to_pay)
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
        orders = [order.to_json() for order in Order.objects.filter(
            address__member__token=self.param("token"),
            status=self.int_param("status", 0)
        ).all()]
        if orders:
            return self.json_response({"code": 0, "data": orders})
        else:
            return self.json_response({"code": 1, "message": "no order found"})

    # http "https://api.it120.cc/tianguoguoxiaopu/order/close?token=c6d64df6-50b6-4012-a7e5-868749fe383a&orderId=133059"
    @api_route('/order/close')
    def close(self):
        order = Order.objects.filter(pk=self.int_param("id"), address__member__token=self.param("token")).first()
        if order:
            order.status = OrderStatus.closed
            order.save()
            return self.json_response({"code": 0, "msg": "success"})

        return self.error(code=1, message="没有此订单")

    # http "https://api.it120.cc/tianguoguoxiaopu/order/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=133068"
    @api_route('/order/detail')
    def detail(self):
        order = Order.objects.filter(pk=self.int_param("id"), address__member__token=self.param("token")).first()
        if order:
            return self.json_response({"code": 0, "data": order.to_json()})

        return self.error(code=1, message="没有此订单")

    @api_route("/order/delivery")
    def delivery(self):
        order = Order.objects.filter(pk=self.int_param("id"), address__member__token=self.param("token")).first()
        if order:
            order.status = OrderStatus.to_evaluate
            order.save()
            return self.json_response({"code": 0, "msg": "success"})

        return self.error(code=1, message="没有此订单")

    # http://192.168.31.80/api/mall/order/reputation?postJsonString=%7B%22token%22%3A%22Fv0IBv%2B3jhD%2Fjoxrdm8sFA%3D%3D%22%2C%22orderId%22%3A%227%22%2C%22reputations%22%3A%5B%5D%7D
    @api_route("/order/reputation")
    def reputation(self):
        obj = json.loads(self.param("json"))
        token = obj.pop("token", None)
        order_id = obj.pop("orderId", None)
        reputations = obj.pop("reputations", None)
        success = False
        if token and reputations and order_id:
            member: Member = Member.objects.filter(token=token).first()
            order: Order = Order.objects.filter(pk=int(order_id)).first()
            item_id_set = set([item.id for item in order.orderitem_set.all()])
            if member and order:
                for re in reputations:
                    item_id = re.pop("id", 0)
                    comment = re.pop('comment', None)
                    remark = re.pop("remark", None)
                    if item_id and comment and remark and item_id in item_id_set:
                        Reputation.objects.create(item_id=item_id, comment=int(comment), remark=remark)
                        success = True
                        item_id_set.remove(item_id)

            if len(item_id_set) == 0:
                order.status = OrderStatus.completed
                order.save()

        return self.ok() if success else self.error()
