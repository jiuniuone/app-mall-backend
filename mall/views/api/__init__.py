import json

from django.conf import settings
from django.urls import path

from acmin.views import api
from acmin.views.api import route as route


def api_route(path, prefix=""):
    return route(path, prefix='/api/mall')


base = settings.BASE_DIR


class ApiView(api.ApiView):
    def load_json(self, file):
        path = f"{base}/data/{file}"
        with open(path, 'r', encoding="UTF-8") as load_f:
            return json.load(load_f)

    def file_json_response(self, file):
        return self.json_response(self.load_json(file))


from acmin.utils.imports import import_sub_classes

import_sub_classes(globals(), __name__, __path__)


def get_urlpatterns():
    get_name = lambda f: "%s.%s" % (f.__module__, f.__qualname__)
    return [path(route, api.get_view(func), name=get_name(func)) for route, func in api.methods.items()]
