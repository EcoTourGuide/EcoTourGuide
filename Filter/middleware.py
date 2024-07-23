from .models import History
import re
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CaptureVisitedSiteMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated:
            if re.match(r'^/explore/', request.path):  # Adjust the path based on your project
                History.objects.create(user=request.user, url=request.get_full_path())
        return response
