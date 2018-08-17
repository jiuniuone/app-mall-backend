# Generated by Django 2.1 on 2018-08-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0013_auto_20180817_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='balance',
            field=models.FloatField(default=0.0, verbose_name='余额'),
        ),
        migrations.AddField(
            model_name='member',
            name='freeze',
            field=models.FloatField(default=0.0, verbose_name='冻结金额'),
        ),
        migrations.AddField(
            model_name='member',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='member',
            name='score',
            field=models.PositiveIntegerField(default=0, verbose_name='积分'),
        ),
        migrations.AddField(
            model_name='member',
            name='sign_continuous_days',
            field=models.PositiveIntegerField(default=0, verbose_name='连续签到天数'),
        ),
        migrations.AlterField(
            model_name='member',
            name='token',
            field=models.CharField(max_length=200, unique=True, verbose_name='标识'),
        ),
    ]
