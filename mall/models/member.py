from .base import Base, models


class Member(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "微信用户"

    list_fields = ["open_id", "nickname", "gender", "country", "province", "city", "balance", "score", "token"]

    open_id = models.CharField("开放ID", max_length=200, unique=True)
    nickname = models.CharField("昵称", max_length=100)
    gender = models.IntegerField("性别")
    language = models.CharField("语言", max_length=100)
    city = models.CharField("城市", max_length=100)
    province = models.CharField("省份", max_length=500)
    country = models.CharField("国家", max_length=200)
    avatar_url = models.URLField("头像地址")
    token = models.CharField("标识", max_length=200, unique=True)
    mobile = models.CharField("手机号码", blank=True, null=True, max_length=20)
    balance = models.FloatField("余额", default=0.0, null=False)
    freeze = models.FloatField("冻结金额", default=0.0, null=False)
    score = models.PositiveIntegerField("积分", default=0, null=False)
    sign_continuous_days = models.PositiveIntegerField("连续签到天数", default=0, null=False)
    last_sign_date = models.DateField("最近签到日期", null=True,blank=True)

    def __str__(self):
        return self.nickname
