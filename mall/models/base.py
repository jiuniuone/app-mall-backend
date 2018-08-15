from django.db import models

from acmin.models import AcminModel


class Base(AcminModel, models.Model):
    class Meta:
        abstract = True
