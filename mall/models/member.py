from .base import Base, models


class Member(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "用户"

    open_id = models.CharField("开放ID", max_length=200, unique=True)
    nickname = models.CharField("昵称", max_length=100)
    gender = models.IntegerField("性别")
    language = models.CharField("语言", max_length=100)
    city = models.CharField("城市", max_length=100)
    province = models.URLField("省份", max_length=500)
    country = models.CharField("国家", max_length=200)
    avatar_url = models.URLField("头像地址")
    token = models.CharField("标识", max_length=200)
