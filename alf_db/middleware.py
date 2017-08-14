from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.conf import settings
import base64


class BasicAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'HTTP_AUTHORIZATION'  in request.META:
            authentication = request.META.get('HTTP_AUTHORIZATION')
            (auth_method, auth) = authentication.split(' ', 1)
            auth = base64.b64decode(auth.strip()).decode('utf-8')
            username, password = auth.split(':', 1)
            if (
                username == settings.BASICAUTH_USERNAME and
                password == settings.BASICAUTH_PASSWORD
                ):
                return self.get_response(request)
            else:
                response =HttpResponse(status=401)
                response['WWW-Authenticate'] = "Basic"
                return response
        else:
                response =HttpResponse(status=401)
                response['WWW-Authenticate'] = "Basic"
                return response