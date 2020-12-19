from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class JsonResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    
    """
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


class CSRFExemptMixin(object):
    """
    A mixin to by pass csrf token validation.
    We do not do this in production.
    This is just to understand requests.
    
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, *kwargs)



class HttpResponseMixin(object):
    """
    A mixin for return appropriate HTTP status code and Json data.
    """
    is_json = False

    def render_to_json_response(self,data,status=200):

        content_type = "text/html"
        if self.is_json:
            content_type = "application/json"

        return HttpResponse(data,content_type=content_type,status=status)