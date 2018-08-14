from acmin.models import AcminModel
from django.db import models

class Category(AcminModel):
    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = "分类"

    name =    models.CharField(max_length=100)
