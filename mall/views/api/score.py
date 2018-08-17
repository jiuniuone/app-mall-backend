from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # http "http://localhost/api/mall/score/send/rule?code=goodReputation"
    @api_route('/score/send/rule')
    def send_rule(self):
        code = self.param("code")
        if code == 'goodReputation':
            return self.file_json_response("/score/send/rule/goodReputation.json")

        return self.json_response({})

    # http "https://api.it120.cc/tianguoguoxiaopu/score/today-signed?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/score/today-signed')
    def today_signed(self):
        # return self.json_response({"code": 700, "msg": "暂无数据"})
        return self.json_response({"code": 0, "data": {"continuous": 1, "dateAdd": "2018-08-14 00:00:00", "id": 45001, "uid": 505853}, "msg": "success"})


