import datetime
import json

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from acmin.utils import attr
from mall.models import *

base = settings.BASE_DIR


def load_json(file):
    path = f"{base}/data/{file}"
    with open(path, 'r', encoding="UTF-8") as load_f:
        return json.load(load_f)


CLEAR = False

app_name='tz'
#app_name = 'tianguoguoxiaopu'
#app_name = 'gqxywsh'
url_prefix = f'https://api.it120.cc/{app_name}'


# https://api.it120.cc/tianguoguoxiaopu/notice/list?pageSize=7
# https://api.it120.cc/gqxywsh/shop/subshop/list
def get(url):
    return requests.get(url).json()


# python manage.py initdata
class Command(BaseCommand):
    def handle(self, *args, **options):
        if CLEAR:
            Category.objects.all().delete()
            Product.objects.all().delete()
            Coupon.objects.all().delete()
            # Config.objects.all().delete()
            Province.objects.all().delete()
            City.objects.all().delete()
            District.objects.all().delete()
            Notice.objects.all()

        self.import_category()
        self.import_product()
        self.import_notice()
        self.import_address()
        self.import_config()
        self.import_coupon()
        self.import_banner()

    def import_banner(self):
        # Product.objects.filter(banner_enable=True).all().delete()
        if len(Product.objects.filter(banner_enable=True).all()): return
        json = get(f"{url_prefix}/banner/list?key=mallName")
        for obj in attr(json, "data", []):
            id = obj["businessId"]
            if id:
                product = self.import_product_by_id(obj["businessId"])
                product.banner_url = obj['picUrl']
                product.banner_enable = True
                product.save()
                print(product)

    def import_coupon(self):
        # if len(Coupon.objects.all()): return
        json = get(f"{url_prefix}/discounts/coupons")
        for obj in attr(json, "data", []):
            Coupon.objects.create(
                name=obj["name"],
                threshold=obj["moneyHreshold"],
                reduce=obj['moneyMin'],
                total=obj['numberTotle'],
                left=obj['numberLeft'],
                member_limit=obj['numberPersonMax'],
                sequence=0,
                expiry_date=12,
                start_date=datetime.datetime.min,
                end_date=datetime.datetime.max,
                enabled=True,

            )

    def import_config(self):
        # Config.objects.all().delete()
        # if len(Config.objects.all()): return
        keys = ["mallName", "recharge_amount_min", "shopPrompt", "shopDelivery", "shopDeliveryPrice", "couponsTitlePicStr", "aboutUsTitle", "servicePhoneNumber", "aboutUsContent", "finderRecommendTtile"]
        for key in keys:
            # json = load_json("config/get-value/couponsTitlePicStr.json")
            json = get(f"{url_prefix}/config/get-value?key={key}")
            print(json)
            data = attr(json, "data")
            if data:
                if not Config.objects.filter(name=key).first():
                    config = Config.objects.create(name=key, title=data['remark'], content=data["value"])
                    print(config)

    def import_address(self):
        # if Province.objects.all(): return
        array = load_json("city.json")
        provinces = []
        cities = []
        disctricts = []
        for obj in array:
            provinces.append(Province(name=obj["name"], id=obj['id']))
            for city in obj.pop("cityList", []):
                cities.append(City(id=city["id"], name=city["name"], province_id=city["pid"]))
                for disctrict in city.pop("districtList", []):
                    disctricts.append(District(id=disctrict["id"], city_id=disctrict["pid"], name=disctrict["name"]))
        Province.objects.bulk_create(provinces)
        City.objects.bulk_create(cities)
        District.objects.bulk_create(disctricts)

    def import_notice(self):
        # if Notice.objects.all(): return
        # json = get(f"{url_prefix}/notice/list?pageSize=500")
        for obj in attr(json, "data.dataList", []):
            data = get(f"{url_prefix}/notice/detail?id={obj['id']}").json()["data"]
            Notice.objects.create(title=data["title"], content=data["content"], start_date=datetime.datetime.min, end_date=datetime.datetime.max)

    def import_category(self):
        # if Category.objects.all(): return
        json = get(f"{url_prefix}/shop/goods/category/all", )
        models = []
        for obj in json["data"]:
            if not Category.objects.filter(pk=obj["id"]).first():
                category = Category(name=obj["name"], sequence=0, id=obj["id"])
                models.append(category)
        Category.objects.bulk_create(models)

    def import_product_by_id(self, id):
        json = get(f"{url_prefix}/shop/goods/detail?id={id}")
        data: dict = json["data"]
        info = data["basicInfo"]
        product = Product.objects.create(
            id=info["id"],
            category_id=info["categoryId"],
            name=info["name"],
            characteristic=info["characteristic"],
            hot=0,
            image_url=info["pic"],
            images='\n'.join([p["pic"] for p in data["pics"]]),
            price=info["minPrice"],
            content=data['content'],
            video_id=info.pop('videoId', None),
        )
        properties = data.pop("properties", [{"name": "规格", "childsCurGoods": [{"name": "默认", "price": product.price}]}])
        for property in properties:
            p = Property.objects.create(product=product, name=property["name"])
            for item in property.pop("childsCurGoods", []):
                PropertyItem.objects.create(property=p, name=item["name"], price=info["minPrice"])

        return product
        # url = f"https://api.it120.cc/tz/shop/goods/reputation?goodsId={id}"
        # print(url)
        # json = get(url).json()

    def import_product(self):
        # if Product.objects.all(): return
        json = get(f"{url_prefix}/shop/goods/list")
        for obj in json["data"]:
            id = obj["id"]
            if not Product.objects.filter(pk=id).first():
                self.import_product_by_id(id)
