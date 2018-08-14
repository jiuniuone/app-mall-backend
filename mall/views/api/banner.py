from mall.views.api import ApiView,api_route


class Resource(ApiView):

    # http "https://api.it120.cc/tianguoguoxiaopu/banner/list?key=mallName"
    @api_route('/banner/list')
    def list(self):
        return self.file_json_response("/banner/list.json")
