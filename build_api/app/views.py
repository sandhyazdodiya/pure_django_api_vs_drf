from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from django.views import View
from .mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize
# Create your views here.


# def detail_view(request):
#     return render() # return JSON response
#     return HttpResponse()


def json_example_view(request):
    '''
    URI ----> for a REST API
    GET ----> Retrieve data
    '''
    data={
        "count" :100,
        "content" : "New contact"
    }
    return JsonResponse(data)
    # another way to send json data using python's json module
    # json_data = json.dumps(data)
    # return HttpResponse(json_data,content_type="application/json")


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data={
        "count" :100,
        "content" : "New contact"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin,View):
    """
    This view is using JsonResponseMixin

    """
    def get(self, request, *args, **kwargs):
        data={
        "count" :100,
        "content" : "New contact"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data ={
            "user" : obj.user.username,
            "content" : obj.content
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type="application/json")


# serialization from view
# class SerializedDetailView(View):
#     def get(self, request, *args, **kwargs):
#         obj = Update.objects.get(id=1)
#         data = serialize('json', [obj,], fields=('user','content'))

#         # data ={
#         #     "user" : obj.user.username,
#         #     "content" : obj.content
#         # }
#         # json_data = json.dumps(data)
#         json_data = data
#         return HttpResponse(json_data, content_type="application/json")


# class SerializedListView(View):
#     def get(self, request, *args, **kwargs):
#         qs = Update.objects.all()
#         data = serialize('json', qs, fields=('user','content'))
#         json_data = data
#         return HttpResponse(json_data, content_type="application/json")


# serialization from model
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")