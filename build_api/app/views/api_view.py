from app.models import Update
from django.views import View
from django.http import HttpResponse
from app.mixins import CSRFExemptMixin, HttpResponseMixin
import json

class UpdateModelDetailAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    is_json = True

    def get(self, request, id, *args, **kwargs):
        id_=id
        obj = Update.objects.get(id=id_)
        json_data = obj.serialize()
        return self.render_to_json_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data={}

        return self.render_to_json_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        json_data={}

        return self.render_to_json_response(json_data,)

    
    def delete(self, request, *args, **kwargs):
        json_data={}

        return self.render_to_json_response(json_data)


class UpdateModelListAPIView(HttpResponseMixin,CSRFExemptMixin,View):

    """
    List View
    Create View

    """
    is_json = True
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return self.render_to_json_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message" : "Unknown data"})
        return self.render_to_json_response(data, status=200)

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message" : "You can not delete entire list."})
        # return HttpResponse(data,content_type="application/json")
        return self.render_to_json_response(data, status=403)


