from .base import Base, models

class Category(Base):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "分类"

    name = models.CharField("名称",max_length=100)
    sequence = models.PositiveSmallIntegerField("顺序")
