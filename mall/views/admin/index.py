import random
import string

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_http_methods

from acmin.models import import_model
from acmin.utils import attr
from mall.models import User

app_name = __name__.split(".")[0]

full_nodes = [

    ("首页", ["User", "Address", "Category", "Config", "Coupon", "MemberCoupon", "Notice", 'Member']),
    ("商品", ["Category", "Product", "Property", "PropertyItem"]),
    ("订单", ["Order", "OrderItem", "LogisticsTrace", "Reputation"]),
    ("物流", ["Province", "City", "District", "Address", "Shipper"]),
]


def get_nodes():
    def to_tuple(node):
        if not isinstance(node, tuple):
            model = import_model(app_name, node)
            node = (node, attr(model, '_meta.verbose_name'), attr(model, 'ROLE'))
        return node

    result = []
    for (name, nodes) in full_nodes:
        nodes = [to_tuple(node) for node in nodes]
        nodes = [node[0:2] for node in nodes]
        if nodes: result.append((name, nodes))
    return result


@login_required
@require_http_methods(["GET"])
def index(request):
    user: User = request.user

    name = attr(user, "cinema.channel.name") or getattr(settings, 'FUNCTION_NAME')
    context = {
        "random": ''.join(random.sample(string.ascii_letters + string.digits, 8)),
        "nodes": get_nodes(),
        "site_name": "玩具商城",
        "copyright": "玩具商城 © 2016-2018",
        "role_name": "管理员",

    }

    template = loader.get_template('index/main.html')
    return HttpResponse(template.render(context, request))
