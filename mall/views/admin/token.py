from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.template.response import HttpResponse
from django.views.decorators.http import require_http_methods

from acmin.views.api import admin_route


@admin_route('/token/')
@login_required
@require_http_methods(["GET"])
def get(request):
    return HttpResponse(content=get_token(request))
