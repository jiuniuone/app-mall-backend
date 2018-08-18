from .base import Base, models
from .product import PropertyItem
from .address import Address

class Order(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单"

    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class OrderItem(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单项"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(PropertyItem, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()