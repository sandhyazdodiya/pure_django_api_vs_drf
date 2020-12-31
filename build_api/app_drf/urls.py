from django.urls import path
from app_drf.views import (
    StatusAPIView,
    StatusDetailAPIView,
    # StatusCreateAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
)

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view(),name="detail"),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('update/<int:pk>', StatusUpdateAPIView.as_view()),
    # path('delete/<int:pk>', StatusDeleteAPIView.as_view()),

]


# Start with
# api/status/ ---> List
# api/status/create ---> Create
# api/status/detail/1 ---> Detail
# api/status/update/1 ---> Update
# api/status/delete/1 ---> Delete


# End with
# api/status/ ---> List
# api/status/1 ---> CURD

# Final
# api/status/ ---> CURD & LS
