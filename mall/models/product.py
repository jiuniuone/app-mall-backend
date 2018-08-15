from .base import Base, models

from .category import Category


class Product(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "商品"

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)
    hot = models.PositiveIntegerField("热度")
    image_url = models.URLField("主图地址", max_length=500)
    images = models.TextField('详情图片')
    banner_url = models.URLField("横幅地址", blank=True, null=True, max_length=500)
    bar_code = models.CharField("条形码地址", null=True, blank=True, max_length=500)
    qr_code = models.CharField("二维码地址", null=True, blank=True, max_length=500)
    video_url = models.URLField("视频地址", max_length=500)
    recommendable = models.BooleanField("推荐？", default=False)
    stores = models.PositiveIntegerField("库存", default=1000)
    price = models.FloatField("价格")
    min_price = models.FloatField("最低价")
    max_price = models.FloatField("最高价")
    order_count = models.PositiveIntegerField("购买次数")
    good_reputation_count = models.PositiveIntegerField("好评次数", default=0)

    commission = models.PositiveIntegerField("分享奖励", default=0)
    commission_type = models.PositiveSmallIntegerField("分享类型", default=0)  # 1:积分奖励，2：现金奖励
    sequence = models.PositiveSmallIntegerField("顺序", default=0)


class Property(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "属性"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=20)  # 颜色，尺码等
    sequence = models.PositiveSmallIntegerField("顺序")


class PropertyItem(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "属性项"

    property = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=20)  # 颜色，尺码等
    price = models.PositiveIntegerField("价格")
    sequence = models.PositiveSmallIntegerField("顺序", default=0)
