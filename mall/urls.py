from functools import partial

import django.apps
from django.urls import path
from acmin.views.admin import get_view
from mall.forms.user import LoginForm
from mall.views.admin import index, user
from mall.views.api import get_urlpatterns


urlpatterns = get_urlpatterns()

app_name = __name__.split(".")[0]

models = [model.__name__ for model in django.apps.apps.get_models() if
    model.__module__.startswith(app_name)]

for name in models:
    prefix = f'{app_name}/{name}'
    view = partial(get_view, app_name, name)
    urlpatterns += [
        path(f'{prefix}/', view("list"), name=f'{name}-list'),
        path(f'{prefix}/export/', view("export"), name=f'{name}-export'),
        path(f'{prefix}/create/', view("create"), name=f'{name}-create'),
        path(f'{prefix}/<int:pk>/', view("update"), name=f'{name}-update'),
        path(f'{prefix}/<int:pk>/delete/', view("delete"), name=f'{name}-delete'),
    ]

urlpatterns += [
    path(f'{app_name}/user/login/', user.LoginView.as_view(success_url='/'), kwargs={'authentication_form': LoginForm}),
    path('', index),

]

# if "runserver" in sys.argv:
#    from .utils.decorators import task
#    @task(start=10, interval=60)
#    def show_trace():
#        from .utils import profile
#        profile.show_trace()
#    show_trace()
