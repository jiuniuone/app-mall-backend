from .member import Base, Member, models


class Province(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "省份/直辖市"

    name = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.name


class City(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "地级市/直辖市区"

    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.name


class District(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "县/县级市/地级市区"

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.name


class Address(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "地址"

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField("详细地址", max_length=500)
    code = models.CharField("邮政编码", max_length=6)
    addressee = models.CharField("收件人", max_length=50)
    phone_number = models.CharField("联系电话", max_length=20)
    is_default = models.BooleanField("默认收货地址？", default=False)

    def to_json(self):
        return {
            "provinceId": self.province.id,
            "provinceStr": self.province.name,
            "address": self.addressee,
            "cityId": self.city.id,
            "cityStr": self.city.name,
            "districtId": self.district.id if self.district else None,
            "areaStr": self.district.name if self.district else None,
            "code": self.code,
            "id": self.id,
            "isDefault": self.is_default,
            "linkMan": self.addressee,
            "mobile": self.phone_number,
        }

    def __str__(self):
        return f"{self.province} {self.city} {self.district if self.district else ''} {self.address}"


class Shipper(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "物流公司"

    name = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.name


class Logistics(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "物流"

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    tracking_number = models.CharField("物流单号", max_length=30)
    fee = models.PositiveIntegerField("费用")


class LogisticsTrace(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "物流跟踪"

    logistics = models.ForeignKey(Logistics, on_delete=models.CASCADE)
    event = models.CharField("事件", max_length=500)
    event_time = models.DateTimeField("时间")
