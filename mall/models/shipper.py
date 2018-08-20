from .base import Base, models


class Shipper(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = "物流公司"
        verbose_name_plural = "物流公司"

    name = models.CharField("名称", max_length=100)
    mobile = models.CharField("联系人电话", null=True, blank=True,max_length=20)

    def __str__(self):
        return self.name
