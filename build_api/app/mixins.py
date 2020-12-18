from django.http import JsonResponse


class JsonResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    
    """
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context