from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"

    # http "https://api.it120.cc/tianguoguoxiaopu/user/amount?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/user/amount')
    def amount(self):
        return self.json_response({"code": 0, "data": {"balance": 0.00, "freeze": 0.00, "score": 50, "totleConsumed": 0.00}, "msg": "success"})

    # http "https://api.it120.cc/tianguoguoxiaopu/user/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route("/user/detail")
    def detail(self):
        return self.file_json_response("/user/detail.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/withDraw/apply?token=c6d64df6-50b6-4012-a7e5-868749fe383a&money=100"
    @api_route('/user/withDraw/apply')
    def apply_withdraw(self):
        return self.json_response({"code": 20001, "msg": "可提现余额不足"})
