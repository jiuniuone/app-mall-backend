from django.db import models

from acmin.models import AcminModel


class Base(AcminModel, models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    modified = models.DateTimeField('更新时间', auto_now=True)
