from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # http "https://api.it120.cc/tianguoguoxiaopu/notice/list?pageSize=7"
    @api_route('/notice/list')
    def list(self):
        return self.json_response({
            "code": 0,
            "data": {
                "totalRow": 1,
                "totalPage": 1,
                "dataList": [
                    {"dateAdd": "2017-10-11 17:06:58", "id": 286, "isShow": True, "title": "活动水果限时买 2 送 1", "userId": 891}
                ]},
            "msg": "success"})

    # http "https://api.it120.cc/tianguoguoxiaopu/notice/detail?id=286"
    @api_route('/notice/detail')
    def detail(self):
        return self.file_json_response("/notice/detail.json")
