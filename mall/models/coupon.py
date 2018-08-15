from .base import Base, models
from .member import Member


class Coupon(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "优惠券"

    name = models.CharField("名称", max_length=100)
    threshold = models.PositiveIntegerField("消费阈值(元）")
    reduce = models.PositiveIntegerField("优惠值(元）")
    total = models.PositiveIntegerField("总数")
    left = models.PositiveIntegerField("剩余数")
    member_limit = models.PositiveIntegerField("每人限领数")
    sequence = models.PositiveSmallIntegerField("顺序")
    expiry_date = models.PositiveSmallIntegerField("有效天数")
    start_date = models.DateField("有效期开始")
    end_date = models.DateField("有效期结束")
    enabled = models.BooleanField("开通？")


class MemberCoupon(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "会员优惠券"

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
