import django.apps
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.views.generic import RedirectView

from mall import urls

for model in django.apps.apps.get_models():
    if not admin.site.is_registered(model):
        admin.site.register(model)


def default(_request):
    return HttpResponseRedirect('/mall/')


urlpatterns = urls.urlpatterns
urlpatterns += [
    path('django-admin/', admin.site.urls),
    path('admin/', default),
    path('mall/', default),
]
