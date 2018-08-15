from .base import Base, models


class Config(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "分类"

    name = models.CharField("名称", max_length=100)
    title = models.CharField("标题", max_length=100)
    content = models.TextField("内容")
