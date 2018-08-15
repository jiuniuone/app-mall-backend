from mall.models import Config
from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"
    @api_route('/config')
    def get_value(self):
        key = self.param("key")
        config = Config.objects.filter(name=key).first()
        if config:
            return self.json_response({
                "code": 0,
                "data": {"title": config.title, "content": config.content},
                "message": "success"
            })
        return self.json_response({"code": 1, "message": "no data"})
