from .base import Base, models
from .product import PropertyItem


class Order(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单"


class OrderItem(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "订单项"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(PropertyItem, on_delete=models.CASCADE)
