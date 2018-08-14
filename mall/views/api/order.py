from mall.views.api import ApiView, api_route


class Resource(ApiView):

    # http "https://api.it120.cc/tianguoguoxiaopu/order/create"
    @api_route('/order/create')
    def create(self):
        post_data = 'token=c6d64df6-50b6-4012-a7e5-868749fe383a&goodsJsonStr=%5B%7B%22goodsId%22%3A15745%2C%22number%22%3A4%2C%22propertyChildIds%22%3A%22639%3A4639%2C%22%2C%22logisticsType%22%3A0%7D%5D&remark=&provinceId=320000&cityId=320400&districtId=320401&address=%E5%97%AF%E5%97%AF&linkMan=%E6%9F%90%E6%9F%90%E6%9F%90&mobile=13522222222&code=132466&calculate=true'
        return self.json_response({
            "code": 0,
            "data": {
                "amountLogistics": 0,
                "score": 0,
                "goodsNumber": 4,
                "free_shipping_for_purchases": 48,
                "isNeedLogistics": True,
                "amountTotle": 40.00
            },
            "msg": "success"
        })

    # http "https://api.it120.cc/tianguoguoxiaopu/order/statistics?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/order/statistics')
    def statistics(self):
        return self.json_response({
            "code": 0,
            "data": {
                "count_id_no_reputation": 0,
                "count_id_no_transfer": 0,
                "count_id_close": 0,
                "count_id_no_pay": 1,
                "count_id_no_confirm": 0,
                "count_id_success": 0
            },
            "msg": "success"
        })

    # http "https://api.it120.cc/tianguoguoxiaopu/order/list?token=c6d64df6-50b6-4012-a7e5-868749fe383a&pageSize=10000&page=1"
    @api_route('/order/list')
    def list(self):
        return self.file_json_response("/order/list.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/order/close?token=c6d64df6-50b6-4012-a7e5-868749fe383a&orderId=133059"
    @api_route('/order/close')
    def close(self):
        return self.json_response({"code": 0, "msg": "success"})

    # http "https://api.it120.cc/tianguoguoxiaopu/order/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=133068"
    @api_route('/order/detail')
    def detail(self):
        return self.file_json_response("/order/detail.json")
