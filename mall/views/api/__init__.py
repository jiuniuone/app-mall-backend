import json

from django.conf import settings
from django.urls import path

from acmin.utils import attr
from acmin.utils.imports import import_sub_classes
from acmin.views import api
from acmin.views.api import route as route

base = settings.BASE_DIR


def api_route(path, prefix=""):
    return route(path, prefix='/api/mall')


class ApiView(api.ApiView):
    def load_json(self, file):
        path = f"{base}/data/{file}"
        with open(path, 'r', encoding="UTF-8") as load_f:
            return json.load(load_f)

    def file_json_response(self, file):
        return self.json_response(self.load_json(file))

    def list_response(self, models, include_fields):
        return self.json_response({"code": 0, "data": [{key: attr(c, key) for key in include_fields} for c in models]})


import_sub_classes(globals(), __name__, __path__)


def get_urlpatterns():
    get_name = lambda f: "%s.%s" % (f.__module__, f.__qualname__)
    return [path(route, api.get_view(func), name=get_name(func)) for route, func in api.methods.items()]
