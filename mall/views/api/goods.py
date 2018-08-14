from mall.views.api import ApiView, api_route


class Resource(ApiView):

    # http "http://localhost/api/mall/shop/goods/category/all"
    @api_route('/shop/goods/category/all')
    def category(self):
        return self.file_json_response("/shop/goods/category/all.json")

    # http "http://localhost/api/mall/shop/goods/kanjia/list"
    @api_route('/shop/goods/kanjia/list')
    def kanjia_list(self):
        return self.file_json_response("/shop/goods/kanjia/list.json")

    # http "http://localhost/api/mall/shop/goods/list?page=1&pageSize=10000&categoryId="
    # 商品列表
    @api_route('/shop/goods/list')
    def list(self):
        return self.file_json_response("/shop/goods/list.json")

    # http "http://localhost/api/mall/shop/goods/detail?id=16155"
    # 商品详情
    @api_route('/shop/goods/detail')
    def detail(self):
        id = self.int_param("id", 0)
        return self.file_json_response("/shop/goods/detail.json")

    # http "http://localhost/api/mall/shop/goods/reputation?goodsId=16155"
    # 好评列表
    @api_route('/shop/goods/reputation')
    def reputation(self):
        id = self.int_param("id", 0)
        return self.file_json_response("/shop/goods/reputation.json")

    # http "http://localhost/api/mall/shop/goods/price?goodsId=15771&propertyChildIds=1795%3A4839%2C"
    # 加入到购物车页面，当选择规格时调用，多少斤，重量
    @api_route('/shop/goods/price')
    def price(self):
        return self.file_json_response("/shop/goods/price.json")
