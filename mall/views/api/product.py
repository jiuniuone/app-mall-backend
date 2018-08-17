from acmin.views.api import to_json
from mall.models import Category, Product
from mall.views.api import ApiView, api_route


class Resource(ApiView):

    # http "http://localhost/api/mall/product/category/all"
    @api_route('/product/category/all')
    def category(self):
        return self.list_response(Category.objects.all(), ["id", "name"])

    # http "http://localhost/api/mall/product/kanjia/list"
    @api_route('/product/kanjia/list')
    def kanjia_list(self):
        return self.file_json_response("/product/kanjia/list.json")

    # http "http://localhost/api/mall/product/list?page=1&pageSize=10000&categoryId="
    # 商品列表
    @api_route('/product/list')
    def list(self):
        query = Product.objects
        category_id = self.int_param("category_id")
        if category_id:
            query = query.filter(category_id=category_id)
        return self.list_response(query.all(), "id,name,image_url,price".split(","))

    # http "http://localhost/api/mall/product/detail?id=16155"
    # 商品详情
    @api_route('/product/detail')
    def detail(self):
        product: Product = Product.objects.filter(pk=self.int_param("id")).first()
        product_obj = to_json(product, ["video_id", "id", "score", "content", "stores", "name", "characteristic", "image_url", "video_url", "price", "order_count", "good_reputation_count"])
        if product:
            if product.images:
                product_obj["images"] = product.images.split("\n")
            properties = []
            for property in product.property_set.all():
                property_obj = to_json(property, ["name", "id"])
                items = []
                for item in property.propertyitem_set.all():
                    items.append(to_json(item, ["name", "price", "id"]))
                property_obj["items"] = items
                properties.append(property_obj)
            product_obj["properties"] = properties

            return self.json_response({"code": 0, "data": product_obj})

        return self.json_response({"code": 1})

    # http "http://localhost/api/mall/product/reputation?goodsId=16155"
    # 好评列表
    @api_route('/product/reputation')
    def reputation(self):
        id = self.int_param("id", 0)
        return self.file_json_response("/product/reputation.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/banner/list?key=mallName"
    @api_route('/banner/list')
    def list(self):
        return self.list_response(Product.objects.filter(banner_enable=True).all(), "id,banner_url".split(","))
