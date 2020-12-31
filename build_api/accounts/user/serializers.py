from django.contrib.auth import get_user_model
from rest_framework import serializers
from app_drf.serializers import StatusInlineSerializer

from rest_framework.reverse import reverse as api_reverse


User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):

    uri  = serializers.SerializerMethodField(read_only = True)
    # status_uri  = serializers.SerializerMethodField(read_only = True)
    status  = serializers.SerializerMethodField(read_only = True)
    # recent_status  = serializers.SerializerMethodField(read_only = True)
    # statuses = serializers.HyperlinkedRelatedField(
    #     source= "status_set" , # Status.objects.filter(user=user)
    #     many = True,
    #     read_only= True,
    #     lookup_field = "id",
    #     view_name= "api-status:detail"
    # )

    statuses = StatusInlineSerializer(source = "status_set", many = True, read_only= True)

    class Meta:
        model = User
        fields =[
            "id",
            "username",
            "statuses",
            "uri",
            # "recent_status",
            # "status_uri",
            "status"
        ]

    # def get_uri(self,obj):
    #     return "/api/users/{id}/".format(id=obj.id)

    def get_uri(self,obj):
        # return api_reverse("<namespace>:<viewname>",kwargs={"username" : obj.username})
        request = self.context.get("request")
        return api_reverse("api-user:detail",kwargs={"username" : obj.username}, request = request)

    def get_status(self,obj):
        request = self.context.get("request")
        limit = 10
        if request:
            limit_query = request.GET.get("limit")
            try:
                limit = int(limit_query)
            except:
                pass


        qs = obj.status_set.all().order_by("-timestamp")
        data ={
            "uri" : self.get_uri(obj) + "status/",
            # "recent" : self.get_recent_status(obj)
            "last" : StatusInlineSerializer(qs.first(),context = {"request" : request}).data,
            "recent" : StatusInlineSerializer(qs[:limit], many = True,context = {"request" : request}).data,
        }
        return data

    # def get_status_uri(self,obj):
    #     return self.get_uri(obj) + "status/"

    # def get_recent_status(self,obj):
    #     qs = obj.status_set.all().order_by("-timestamp")[:10] # Status.objects.filter(user=obj)
    #     return StatusInlineSerializer(qs, many = True).data
