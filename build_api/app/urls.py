from django.urls import path
from .views.json_view import (json_example_view, 
                    JsonCBV, 
                    JsonCBV2,
                    SerializedDetailView,
                    SerializedListView,)

from .views.api_view import (UpdateModelDetailAPIView, UpdateModelListAPIView)

urlpatterns = [
    path('json-example/', json_example_view),
    path('json/cbv', JsonCBV.as_view()),
    path('json/cbv2', JsonCBV2.as_view()),
    path('json/serialized/list', SerializedListView.as_view()),
    path('json/serialized/detail', SerializedDetailView.as_view()),


    path('api/updates/<int:id>/', UpdateModelDetailAPIView.as_view()),
    path('api/updates/', UpdateModelListAPIView.as_view()),



]
