from django.contrib.auth import get_user_model
from rest_framework import permissions,generics,pagination
from accounts.permissions import AnnonPermissionOnly
from accounts.user.serializers import UserDetailSerializer

from rest_framework.response import Response

from app_drf.serializers import StatusInlineSerializer
from app_drf.models import Status

from app_drf.views import StatusAPIView


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_active = True)
    lookup_field = "username"

    def get_serializer_context(self):
        return {"request" : self.request}



class UserStatusAPIView(StatusAPIView):
    serializer_class = StatusInlineSerializer
    # pagination_class = BuildAPIPagination
    # search_fields = ("user__username","content")
    # ordering_fields = ("user__username","timestamp")

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username",None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username = username)


    # def post(self, request, *args, **kwargs):
    #     return Response({"detail" : "Not allowed here"}, status = 400)

# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class = StatusInlineSerializer
#     # pagination_class = BuildAPIPagination
#     search_fields = ("user__username","content")
#     ordering_fields = ("user__username","timestamp")

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get("username",None)
#         if username is None:
#             return Status.objects.none()
#         return Status.objects.filter(user__username = username)