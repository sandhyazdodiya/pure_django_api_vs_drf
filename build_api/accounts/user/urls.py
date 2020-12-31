from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from accounts.user.views import UserDetailAPIView,UserStatusAPIView


urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name = "detail"),
    path('<str:username>/status/', UserStatusAPIView.as_view(), name = "status-list"),

]
