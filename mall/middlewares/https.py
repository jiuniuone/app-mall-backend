import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class HttpsCheckMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.get_response = get_response

    def process_response(self, request, response):
        meta = request.META
        ip = meta.get('HTTP_X_FORWARDED_FOR') or meta.get('REMOTE_ADDR')
        if "127.0.0.1" == ip or request.get_full_path().startswith("/api"):
            return response
        logger.error("invalid access,path=%s,ip=%s" % (request.get_full_path(), ip))
        return HttpResponse("error")
