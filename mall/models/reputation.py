from .base import Base, models

from .order import OrderItem


class Comment:
    negative = 0
    moderate = 1
    positive = 2

    choices = (
        (positive, "好评"),
        (moderate, "中评"),
        (negative, "差评"),
    )


class Reputation(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "评价"

    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    comment = models.SmallIntegerField(choices=Comment.choices, default=Comment.positive)
    remark = models.CharField(max_length=500)
