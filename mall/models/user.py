from django.contrib.auth.models import AbstractUser
from django.db import models

from acmin.models import ModelMixin


class User(ModelMixin, AbstractUser):
    class Meta:
        ordering = ['-id']
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    creatable = True
    editable = True
    removable = True
    list_fields = ['title']
    form_fields = list_fields  # + ['is_staff', 'is_active']
    search_fields = ['title']

    title = models.CharField('名称', max_length=50, blank=False, null=False)
    mobile = models.CharField("mobile",max_length=100)

    def __str__(self):
        return self.title
