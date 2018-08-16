from .base import Base, models


class Member(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "用户"

    open_id = models.CharField("开放ID", max_length=200,unique=True)
    name = models.CharField("名称", max_length=100)
    province = models.CharField("省份", max_length=100)
    city = models.CharField("城市", max_length=100)
    nickname = models.CharField("昵称", max_length=100)
    avatar_url = models.URLField("头像地址", max_length=500)
    token = models.CharField("标识", max_length=200 )
