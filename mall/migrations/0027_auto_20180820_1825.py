# Generated by Django 2.1 on 2018-08-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0026_auto_20180820_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipper',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='联系人电话'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fee',
            field=models.FloatField(default=0.0, verbose_name='费用'),
        ),
    ]