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


# python manage.py initdata
class Command(BaseCommand):
    def handle(self, *args, **options):
        if CLEAR:
            Category.objects.all().delete()
            Product.objects.all().delete()

        self.import_category()
        self.import_product()
        self.import_notice()
        self.import_address()
        self.import_config()
        self.import_coupon()

    def import_coupon(self):
        if len(Coupon.objects.all()): return
        response = requests.get("https://api.it120.cc/tz/discounts/coupons")
        for obj in attr(response.json(), "data", []):
            Coupon.objects.create(
                id=obj["id"],
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
                enabled=True
            )

    def import_config(self):
        if len(Config.objects.all()): return
        keys = ["mallName", "recharge_amount_min", "shopPrompt", "shopDelivery", "shopDeliveryPrice", "couponsTitlePicStr", "aboutUsTitle", "servicePhoneNumber", "aboutUsContent", "finderRecommendTtile"]
        for key in keys:
            json = load_json("config/get-value/couponsTitlePicStr.json")
            # json = requests.get(f"https://api.it120.cc/tz/config/get-value?key={key}").json()
            print(json)
            data = attr(json, "data")
            if data:
                config = Config.objects.create(name=key, title=data['remark'], content=data["value"])
                print(config)

    def import_address(self):
        if Province.objects.all(): return
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
        if len(Notice.objects.all()) == 0:
            response = requests.get("https://api.it120.cc/tz/notice/list?pageSize=500")
            for obj in attr(response.json(), "data.dataList", []):
                data = requests.get(f"https://api.it120.cc/tz/notice/detail?id={obj['id']}").json()["data"]
                Notice.objects.create(title=data["title"], content=data["content"], start_date=datetime.datetime.min, end_date=datetime.datetime.max)

    def import_category(self):
        if len(Category.objects.all()) == 0:
            response = requests.get("https://api.it120.cc/tz/shop/goods/category/all", )
            models = []
            for obj in response.json()["data"]:
                category = Category(name=obj["name"], sequence=0, id=obj["id"])
                models.append(category)
            Category.objects.bulk_create(models)

    def import_product(self):
        if len(Product.objects.all()) == 0:
            response = requests.get("https://api.it120.cc/tz/shop/goods/list")
            for obj in response.json()["data"]:
                id = obj["id"]
                url = f"https://api.it120.cc/tz/shop/goods/detail?id={id}"
                print(url)
                response = requests.get(url)
                data: dict = response.json()["data"]
                info = data["basicInfo"]
                pics = data["pics"]
                product = Product.objects.create(
                    id=info["id"],
                    category_id=info["categoryId"],
                    name=info["name"],
                    characteristic=info["characteristic"],
                    hot=0,
                    image_url=info["pic"],
                    images='\n'.join([p["pic"] for p in data["pics"]]),
                    price=info["minPrice"],
                )

                for property in data.pop("properties", []):
                    p = Property.objects.create(product=product, name=property["name"])
                    for item in property.pop("childsCurGoods", []):
                        PropertyItem.objects.create(property=p, name=item["name"], price=info["minPrice"])
