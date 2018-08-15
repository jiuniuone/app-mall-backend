from mall.models import Notice
from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # http "https://api.it120.cc/tianguoguoxiaopu/notice/list?pageSize=7"
    @api_route('/notice/list')
    def list(self):
        return self.json_response({"code": 0, "data": [{"id": n.id, "title": n.title} for n in Notice.objects.all()]})

    # http "http://192.168.31.100/api/mall/notice/detail?id=1"
    @api_route('/notice/detail')
    def detail(self):
        notice = Notice.objects.filter(pk=self.int_param("id")).first()
        if notice:
            return self.json_response({
                "code": 0,
                "data": {
                    "title": notice.title,
                    "content": notice.content
                }
            })
        return self.json_response({"code": 1})
