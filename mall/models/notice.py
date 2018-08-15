from .base import Base, models


class Notice(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "用户"

    title = models.CharField("标题", max_length=100)
    content = models.TextField("详情")
    start_date = models.DateField("有效期开始")
    end_date = models.DateField("有效期结束")
    enabled = models.BooleanField("开通？", default=True)

    def __str__(self):
        return self.title
