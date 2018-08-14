from mall.views.api import ApiView,api_route


class Resource(ApiView):

    # http "https://api.it120.cc/tianguoguoxiaopu/pay/wxapp/get-pay-data?token=c6d64df6-50b6-4012-a7e5-868749fe383a&money=50&remark=%E6%94%AF%E4%BB%98%E8%AE%A2%E5%8D%95%20%EF%BC%9A133068&payName=%E5%9C%A8%E7%BA%BF%E6%94%AF%E4%BB%98&nextAction=%7B%22type%22%3A0%2C%22id%22%3A133068%7D"
    #@api_route("")
    def pay_wxapp(self):
        return self.json_response({
            "code": 0,
            "data": {
                "timeStamp": "1534236398396",
                "outTradeId": "ZF1808141408189969",
                "appid": "wx246983b8b8332e17",
                "sign": "2CE92B4E730421B6F3AA6BED2EF14291",
                "prepayId": "wx14164638369930c6e22d202e0205447947",
                "nonceStr": "ZNYifTwacUPl4V5eAwBSmEY47s2iVb"
            },
            "msg": "success"
        })

    # http "https://api.it120.cc/tianguoguoxiaopu/pay/wxapp/get-pay-data?token=c6d64df6-50b6-4012-a7e5-868749fe383a&money=100&remark=%E5%9C%A8%E7%BA%BF%E5%85%85%E5%80%BC&payName=%E5%9C%A8%E7%BA%BF%E6%94%AF%E4%BB%98&nextAction=%7B%7D"
    @api_route('/pay/wxapp/get-pay-data')
    def get_pay_data(self):
        return self.json_response({
            "code": 0,
            "data": {
                "timeStamp": "1534238015111",
                "outTradeId": "ZF1808141576175820",
                "appid": "wx246983b8b8332e17",
                "sign": "887D76E3773BD28163988AB9F0C3B71F",
                "prepayId": "wx141713350809073f3c65047f1549767533",
                "nonceStr": "pqYDHtpe31AjKzxibmVbVwTqeVEXHD"
            },
            "msg": "success"
        })
