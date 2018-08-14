from mall.views.api import ApiView, api_route


class Resource(ApiView):

    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/my?token=c6d64df6-50b6-4012-a7e5-868749fe383a&status=0"
    @api_route('/discounts/my')
    def my(self):
        # return self.json_response({"code": 700, "msg": "暂无数据"})
        return self.file_json_response("/discounts/my.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/coupons?type="
    @api_route('/discounts/coupons')
    def coupons(self):
        return self.file_json_response("/discounts/coupons.json")

    # 领优惠券
    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/fetch?id=864&token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/discounts/fetch')
    def fetch(self):
        return self.file_json_response("/discounts/fetch.json")
