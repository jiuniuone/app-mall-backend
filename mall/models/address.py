from .member import Base, Member, models


class Province(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "省份/直辖市"

    name = models.CharField(Member, max_length=100)


class City(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "地级市/直辖市区"

    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(Member, max_length=100)


class District(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "县/县级市/地级市区"

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(Member, max_length=100)


class Address(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "分类"

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    province_id = models.PositiveIntegerField("省份ID")
    province_name = models.CharField("省份名称", max_length=100)

    city_id = models.PositiveIntegerField("地级市ID")
    city_name = models.CharField("地级市名称", max_length=100)

    district_id = models.PositiveIntegerField("市区ID")
    district_name = models.CharField("市区名称", max_length=100)

    address = models.CharField("详细地址", max_length=500)

    code = models.CharField("邮政编码", max_length=6)

    addressee = models.CharField("收件人", max_length=50)
    phone_number = models.CharField("联系电话", max_length=20)

    is_default = models.BooleanField("默认收货地址？", default=False)
