from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"
    @api_route('/config/get-value')
    def get_value(self):
        key = self.param("key")
        if key == 'mallName':
            return self.file_json_response("/config/get-value/mallName.json")
        if key == 'recharge_amount_min':
            return self.file_json_response("/config/get-value/recharge_amount_min.json")
        if key == 'shopPrompt':
            return self.file_json_response("/config/get-value/shopPrompt.json")
        if key == 'shopDelivery':
            return self.file_json_response("/config/get-value/shopDelivery.json")

        if key == 'shopDeliveryPrice':
            return self.file_json_response("/config/get-value/shopDeliveryPrice.json")
        return self.json_response({})

    # http "http://localhost/api/mall/shop/goods/category/all"
    @api_route('/shop/goods/category/all')
    def shop_category_all(self):
        return self.file_json_response("/shop/goods/category/all.json")

    # http "http://localhost/api/mall/shop/goods/kanjia/list"
    @api_route('/shop/goods/kanjia/list')
    def shop_kanjia_list(self):
        return self.file_json_response("/shop/goods/kanjia/list.json")

    # http "http://localhost/api/mall/score/send/rule?code=goodReputation"
    @api_route('/score/send/rule?code=goodReputation')
    def score_send_rule(self):
        code = self.param("code")
        if code == 'goodReputation':
            return self.file_json_response("/score/send/rule/goodReputation.json")

        return self.json_response({})

    # http "http://localhost/api/mall/shop/goods/list?page=1&pageSize=10000&categoryId="
    # 商品列表
    @api_route('/shop/goods/list')
    def shop_goods_list(self):
        return self.file_json_response("/shop/goods/list.json")

    # http "http://localhost/api/mall/shop/goods/detail?id=16155"
    # 商品详情
    @api_route('/shop/goods/detail')
    def shop_goods_detail(self):
        id = self.int_param("id", 0)
        return self.file_json_response("/shop/goods/detail.json")

    # http "http://localhost/api/mall/shop/goods/detail?id=16155"
    # 好评列表
    @api_route('/shop/goods/reputation?goodsId=16155')
    def shop_goods_detail(self):
        id = self.int_param("id", 0)
        return self.file_json_response("/shop/goods/reputation.json")

    # http "http://localhost/api/mall/shop/goods/price?goodsId=15771&propertyChildIds=1795%3A4839%2C"
    # 加入到购物车页面，当选择规格时调用，多少斤，重量
    @api_route('/shop/goods/price')
    def shop_goods_price(self):
        return self.file_json_response("/shop/goods/price.json")

    @api_route('/user/shipping-address/default?token=c6d64df6-50b6-4012-a7e5-868749fe383a')
    def shop_goods_price(self):
        return self.file_json_response("/shop/goods/price.json")
