# Generated by Django 2.1 on 2018-08-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0015_auto_20180817_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_sign_date',
            field=models.DateField(null=True, verbose_name='最近签到日期'),
        ),
    ]
