from .base import Base, models

from .category import Category


class Product(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "商品"

    list_fields = ['name', 'characteristic', 'recommendable', 'stores', 'price', 'order_count', 'good_reputation_count', 'banner_enable']

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)
    characteristic = models.CharField("特色", max_length=1000)
    hot = models.PositiveIntegerField("热度", default=0)
    image_url = models.URLField("主图地址", max_length=500)
    images = models.TextField('详情图片', null=True, blank=True)
    banner_url = models.URLField("横幅地址", blank=True, null=True, max_length=500)
    bar_code = models.CharField("条形码地址", null=True, blank=True, max_length=500)
    qr_code = models.CharField("二维码地址", null=True, blank=True, max_length=500)
    video_url = models.URLField("视频地址", null=True, blank=True, max_length=500)
    recommendable = models.BooleanField("推荐？", default=False)
    stores = models.PositiveIntegerField("库存", default=1000)
    price = models.FloatField("价格")
    min_price = models.FloatField("最低价", default=0)
    max_price = models.FloatField("最高价", default=0)
    order_count = models.PositiveIntegerField("购买次数", default=0)
    good_reputation_count = models.PositiveIntegerField("好评次数", default=0)
    banner_enable = models.BooleanField("横幅显示？", default=False)
    commission = models.PositiveIntegerField("分享奖励", default=0)
    commission_type = models.PositiveSmallIntegerField("分享类型", default=0)  # 1:积分奖励，2：现金奖励
    sequence = models.PositiveSmallIntegerField("顺序", default=0)
    score = models.PositiveIntegerField("Score", default=200)
    content = models.TextField("渲染内容", null=True, blank=True)
    video_id = models.CharField("视频ID", null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name


class Property(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "属性"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=20)  # 颜色，尺码等
    sequence = models.PositiveSmallIntegerField("顺序", default=0)

    def __str__(self):
        return f"{self.product} {self.name}"


class PropertyItem(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "属性项"

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=20)  # 颜色，尺码等
    price = models.PositiveIntegerField("价格")
    sequence = models.PositiveSmallIntegerField("顺序", default=0)

    def __str__(self):
        return f"{self.property} {self.name}"
