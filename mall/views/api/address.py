from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"

    # http "https://api.it120.cc/tianguoguoxiaopu/user/shipping-address/list?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/user/shipping-address/list')
    def list(self):
        return self.json_response({"code": 700, "msg": "暂无数据"})

    # http "https://api.it120.cc/tianguoguoxiaopu/user/shipping-address/update?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=31730&isDefault=true"
    @api_route('/user/shipping-address/update')
    def update(self):
        return self.json_response({"code": 0, "msg": "success"})

    # http "http://localhost/api/mall/user/shipping-address/default?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/user/shipping-address/default')
    def default(self):
        return self.file_json_response("/user/shipping-address/default.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/shipping-address/add?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=0&provinceId=320000&cityId=320400&districtId=320401&linkMan=%E6%9F%90%E6%9F%90%E6%9F%90&address=%E5%97%AF%E5%97%AF&mobile=13522222222&code=132466&isDefault=true"
    @api_route('/user/shipping-address/add')
    def add(self):
        return self.file_json_response("/user/shipping-address/add.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/shipping-address/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=31730"
    @api_route('/user/shipping-address/detail')
    def default(self):
        return self.file_json_response("/user/shipping-address/detail.json")
