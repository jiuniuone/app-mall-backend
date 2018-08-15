from .base import Base, models

from .order import Order


class Reputation(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "评价"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)  # 好评，中评，差评
    remark = models.CharField(max_length=500)
