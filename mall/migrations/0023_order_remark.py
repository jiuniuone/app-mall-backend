# Generated by Django 2.1 on 2018-08-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0022_order_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='remark',
            field=models.TextField(default=1, verbose_name='备注'),
            preserve_default=False,
        ),
    ]
