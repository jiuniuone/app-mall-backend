from .base import Base, models


class Member(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "用户"

    name = models.CharField("名称", max_length=100)
    province = models.CharField("省份", max_length=100)
    city = models.CharField("城市", max_length=100)
    nickname = models.CharField("昵称", max_length=100)
    avatar_url = models.URLField("头像地址", max_length=500)
