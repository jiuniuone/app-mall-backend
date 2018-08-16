from .base import Base, models


class Config(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "配置"

    name = models.CharField("名称", max_length=100, unique=True)
    title = models.CharField("标题", max_length=100)
    content = models.TextField("内容")

    def __str__(self):
        return f"{self.name},{self.title},{self.content}"
