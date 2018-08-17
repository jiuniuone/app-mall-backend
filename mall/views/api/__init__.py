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

    def list_response(self, objs, include_fields):
        return self.json_response({"code": 0, "data": [{key: attr(c, key) for key in include_fields} for c in objs]})

    def to_json(self, obj, include_fields):
        return {"code": 0, "data": {key: attr(obj, key) for key in include_fields}}

    def obj_response(self, obj, include_fields):
        return self.json_response(self.to_json(obj, include_fields))

    def error(self, code: int, message: str = None):
        return self.json_response({"code": code, "message": message})

    def ok(self):
        return self.json_response({"code": 0})


import_sub_classes(globals(), __name__, __path__)


def get_urlpatterns():
    get_name = lambda f: "%s.%s" % (f.__module__, f.__qualname__)
    return [path(route, api.get_view(func), name=get_name(func)) for route, func in api.methods.items()]
