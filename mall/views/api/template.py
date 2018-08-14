from mall.views.api import ApiView, api_route


class Resource(ApiView):


    # http "https://api.it120.cc/tianguoguoxiaopu/template-msg/put"
    @api_route("template-msg/put")
    def template_msg_put(self):
        post_data = 'token=c6d64df6-50b6-4012-a7e5-868749fe383a&type=0&module=order&business_id=133059&trigger=-1&template_id=gVeVx5mthDBpIuTsSKaaotlFtl5sC4I7TZmx2PtEYn8&form_id=f7bee5c0ab688f6b60e19a58b038b9fb&url=pages%2Fclassification%2Findex&postJsonString=%7B%22keyword1%22%3A%7B%22value%22%3A%22OD1808141519729102%22%2C%22color%22%3A%22%23173177%22%7D%2C%22keyword2%22%3A%7B%22value%22%3A%222018-08-14%2016%3A05%3A42%22%2C%22color%22%3A%22%23173177%22%7D%2C%22keyword3%22%3A%7B%22value%22%3A%2240%E5%85%83%22%2C%22color%22%3A%22%23173177%22%7D%2C%22keyword4%22%3A%7B%22value%22%3A%22%E5%B7%B2%E5%85%B3%E9%97%AD%22%2C%22color%22%3A%22%23173177%22%7D%2C%22keyword5%22%3A%7B%22value%22%3A%22%E6%82%A8%E5%8F%AF%E4%BB%A5%E9%87%8D%E6%96%B0%E4%B8%8B%E5%8D%95%EF%BC%8C%E8%AF%B7%E5%9C%A830%E5%88%86%E9%92%9F%E5%86%85%E5%AE%8C%E6%88%90%E6%94%AF%E4%BB%98%22%2C%22color%22%3A%22%23173177%22%7D%7D&emphasis_keyword=keyword4.DATA'

        return self.json_response({"code": 0, "msg": "success"})

