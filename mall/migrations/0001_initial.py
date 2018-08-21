# Generated by Django 2.1 on 2018-08-21 13:02

import acmin.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('title', models.CharField(max_length=50, verbose_name='名称')),
                ('mobile', models.CharField(max_length=100, verbose_name='mobile')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'ordering': ['-id'],
            },
            bases=(acmin.models.ModelMixin, models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('address', models.CharField(max_length=500, verbose_name='详细地址')),
                ('code', models.CharField(max_length=6, verbose_name='邮政编码')),
                ('addressee', models.CharField(max_length=50, verbose_name='收件人')),
                ('phone_number', models.CharField(max_length=20, verbose_name='联系电话')),
                ('is_default', models.BooleanField(default=False, verbose_name='默认收货地址？')),
            ],
            options={
                'verbose_name': '地址',
                'verbose_name_plural': '地址',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('sequence', models.PositiveSmallIntegerField(verbose_name='顺序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name': '地级市/直辖市区',
                'verbose_name_plural': '地级市/直辖市区',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '配置',
                'verbose_name_plural': '配置',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('threshold', models.PositiveIntegerField(verbose_name='消费阈值(元）')),
                ('reduce', models.PositiveIntegerField(verbose_name='优惠值(元）')),
                ('total', models.PositiveIntegerField(verbose_name='总数')),
                ('left', models.PositiveIntegerField(verbose_name='剩余数')),
                ('member_limit', models.PositiveIntegerField(verbose_name='每人限领数')),
                ('sequence', models.PositiveSmallIntegerField(verbose_name='顺序')),
                ('expiry_date', models.PositiveSmallIntegerField(verbose_name='有效天数')),
                ('start_date', models.DateField(verbose_name='有效期开始')),
                ('end_date', models.DateField(verbose_name='有效期结束')),
                ('enabled', models.BooleanField(verbose_name='开通？')),
            ],
            options={
                'verbose_name': '优惠券',
                'verbose_name_plural': '优惠券',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.City')),
            ],
            options={
                'verbose_name': '县/县级市/地级市区',
                'verbose_name_plural': '县/县级市/地级市区',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='LogisticsTrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('event', models.CharField(max_length=500, verbose_name='事件')),
                ('event_time', models.DateTimeField(verbose_name='时间')),
            ],
            options={
                'verbose_name': '物流跟踪',
                'verbose_name_plural': '物流跟踪',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('open_id', models.CharField(max_length=200, unique=True, verbose_name='开放ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='昵称')),
                ('gender', models.IntegerField(verbose_name='性别')),
                ('language', models.CharField(max_length=100, verbose_name='语言')),
                ('city', models.CharField(max_length=100, verbose_name='城市')),
                ('province', models.CharField(max_length=500, verbose_name='省份')),
                ('country', models.CharField(max_length=200, verbose_name='国家')),
                ('avatar_url', models.URLField(verbose_name='头像地址')),
                ('token', models.CharField(max_length=200, unique=True, verbose_name='标识')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号码')),
                ('balance', models.FloatField(default=0.0, verbose_name='余额')),
                ('freeze', models.FloatField(default=0.0, verbose_name='冻结金额')),
                ('score', models.PositiveIntegerField(default=0, verbose_name='积分')),
                ('sign_continuous_days', models.PositiveIntegerField(default=0, verbose_name='连续签到天数')),
                ('last_sign_date', models.DateField(blank=True, null=True, verbose_name='最近签到日期')),
            ],
            options={
                'verbose_name': '微信用户',
                'verbose_name_plural': '微信用户',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='MemberCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Coupon')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Member')),
            ],
            options={
                'verbose_name': '会员优惠券',
                'verbose_name_plural': '会员优惠券',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='详情')),
                ('start_date', models.DateField(verbose_name='有效期开始')),
                ('end_date', models.DateField(verbose_name='有效期结束')),
                ('enabled', models.BooleanField(default=True, verbose_name='开通？')),
            ],
            options={
                'verbose_name': '通知',
                'verbose_name_plural': '通知',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('order_number', models.CharField(max_length=20, unique=True, verbose_name='订单号')),
                ('fee', models.FloatField(default=0.0, verbose_name='费用')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '待付款'), (1, '待发货'), (2, '待收货'), (3, '待评价'), (4, '已完成'), (5, '已取消')], default=0, verbose_name='状态')),
                ('remark', models.TextField(verbose_name='备注')),
                ('logistics_fee', models.PositiveIntegerField(default=10, verbose_name='运费')),
                ('tracking_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='物流单号')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Address')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('amount', models.PositiveIntegerField(verbose_name='数量')),
            ],
            options={
                'verbose_name': '订单项',
                'verbose_name_plural': '订单项',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '待付款'), (1, '待发货'), (2, '待收货'), (3, '待评价'), (4, '已完成'), (5, '已取消')], default=0, verbose_name='状态')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Order')),
            ],
            options={
                'verbose_name': '订单项',
                'verbose_name_plural': '订单项',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('characteristic', models.CharField(max_length=1000, verbose_name='特色')),
                ('hot', models.PositiveIntegerField(default=0, verbose_name='热度')),
                ('image_url', models.URLField(max_length=500, verbose_name='主图地址')),
                ('images', models.TextField(blank=True, null=True, verbose_name='详情图片')),
                ('banner_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='横幅地址')),
                ('bar_code', models.CharField(blank=True, max_length=500, null=True, verbose_name='条形码地址')),
                ('qr_code', models.CharField(blank=True, max_length=500, null=True, verbose_name='二维码地址')),
                ('video_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='视频地址')),
                ('recommendable', models.BooleanField(default=False, verbose_name='推荐？')),
                ('stores', models.PositiveIntegerField(default=1000, verbose_name='库存')),
                ('price', models.FloatField(verbose_name='价格')),
                ('min_price', models.FloatField(default=0, verbose_name='最低价')),
                ('max_price', models.FloatField(default=0, verbose_name='最高价')),
                ('order_count', models.PositiveIntegerField(default=0, verbose_name='购买次数')),
                ('good_reputation_count', models.PositiveIntegerField(default=0, verbose_name='好评次数')),
                ('banner_enable', models.BooleanField(default=False, verbose_name='横幅显示？')),
                ('commission', models.PositiveIntegerField(default=0, verbose_name='分享奖励')),
                ('commission_type', models.PositiveSmallIntegerField(default=0, verbose_name='分享类型')),
                ('sequence', models.PositiveSmallIntegerField(default=0, verbose_name='顺序')),
                ('score', models.PositiveIntegerField(default=200, verbose_name='Score')),
                ('content', models.TextField(blank=True, null=True, verbose_name='渲染内容')),
                ('video_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='视频ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Category')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('sequence', models.PositiveSmallIntegerField(default=0, verbose_name='顺序')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Product')),
            ],
            options={
                'verbose_name': '属性',
                'verbose_name_plural': '属性',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='PropertyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('price', models.PositiveIntegerField(verbose_name='价格')),
                ('sequence', models.PositiveSmallIntegerField(default=0, verbose_name='顺序')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Property')),
            ],
            options={
                'verbose_name': '属性项',
                'verbose_name_plural': '属性项',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name': '省份/直辖市',
                'verbose_name_plural': '省份/直辖市',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Reputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.SmallIntegerField(choices=[(2, '好评'), (1, '中评'), (0, '差评')], default=2)),
                ('remark', models.CharField(max_length=500)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.OrderItem')),
            ],
            options={
                'verbose_name': '评价',
                'verbose_name_plural': '评价',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='联系人电话')),
            ],
            options={
                'verbose_name': '物流公司',
                'verbose_name_plural': '物流公司',
                'ordering': ['-id'],
            },
            bases=(acmin.models.AcminModel, models.Model),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.PropertyItem'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.Shipper', verbose_name='物流公司'),
        ),
        migrations.AddField(
            model_name='logisticstrace',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Order'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Province'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mall.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Member'),
        ),
        migrations.AddField(
            model_name='address',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.Province'),
        ),
    ]
