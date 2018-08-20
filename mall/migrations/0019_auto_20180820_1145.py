# Generated by Django 2.1 on 2018-08-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0018_auto_20180820_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='address',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='city',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='city',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='config',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='config',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='district',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='district',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='member',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='member',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='membercoupon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='membercoupon',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='notice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='notice',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='order',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='property',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='property',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='propertyitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='propertyitem',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='province',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='province',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='reputation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='reputation',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]