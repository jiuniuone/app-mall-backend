from acmin.utils import first, attr
from .base import Base, models
from .product import PropertyItem
from .shipper import Shipper
from .address import Address


class OrderStatus:
    to_pay = 0
    to_deliver = 1
    to_receive = 2
    to_evaluate = 3
    completed = 4
    closed = 5
    choices = (
        (to_pay, "待付款"),
        (to_deliver, "待发货"),
        (to_receive, "待收货"),
        (to_evaluate, "待评价"),
        (completed, "已完成"),
        (closed, "已取消"),
    )


class Order(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单"

    list_fields = ["order_number", "fee", "logistics_fee", "status", "shipper", "tracking_number"]

    order_number = models.CharField("订单号", unique=True, max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, null=True, blank=True, verbose_name="物流公司")
    fee = models.FloatField("费用", default=0.0)
    status = models.PositiveSmallIntegerField("状态", choices=OrderStatus.choices, default=OrderStatus.to_pay)
    remark = models.TextField("备注")
    logistics_fee = models.PositiveIntegerField("运费", default=10)
    tracking_number = models.CharField("物流单号", max_length=30, null=True, blank=True)

    @property
    def total_fee(self):
        return self.fee + self.logistics_fee

    def __str__(self):
        return self.order_number

    @property
    def status_name(self):
        return first([e[1] for e in OrderStatus.choices if e[0] == self.status])

    def to_json(self):
        return {
            "id": self.id,
            "address": self.address.to_json(),
            "items": [item.to_json() for item in self.orderitem_set.all()],
            "status": self.status,
            "status_name": self.status_name,
            "created": self.created.strftime("%Y-%m-%d %H:%M:%S"),
            "order_number": self.order_number,
            "remark": self.remark,
            "fee": self.fee,
            "logistics_fee": self.logistics_fee,
            "total_fee": self.total_fee,
            "shipper": attr(self.shipper, "name"),
            "tracking_number": self.tracking_number,
            "logistics_traces": [l.to_json() for l in self.logisticstrace_set.order_by("-event_time").all()]
        }


class OrderLog(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单项"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField("状态", choices=OrderStatus.choices, default=OrderStatus.to_pay)


class LogisticsTrace(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "物流跟踪"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    event = models.CharField("事件", max_length=500)
    event_time = models.DateTimeField("时间")

    def to_json(self):
        return {
            "event": self.event,
            "event_time": self.event_time.strftime("%Y-%m-%d %H:%M:%S")
        }


class OrderItem(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单项"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(PropertyItem, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("数量")

    def to_json(self):
        property_item: PropertyItem = self.item
        property = property_item.property
        product = property.product
        return {
            "order_id": self.order.id,
            "product_id": product.id,
            "product_name": product.name,
            "product_image": product.image_url,
            "property_name": property.name,
            "property_id": property.id,
            "item_id": property_item.id,
            "item_name": property_item.name,
            "item_price": property_item.price,
            "amount": self.amount,
        }
