from rest_framework import serializers
from app_drf.models import Status
from accounts.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse

"""
Serializer ---> Converts to Json
Serializer ---> Validates data
"""

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


# class StatusInlineSerializer(serializers.ModelSerializer):
#     uri  = serializers.SerializerMethodField(read_only = True)

#     class Meta:
#         model = Status
#         fields =[
#             "uri",
#             "id",
#             "content",
#             "image"
#         ]

#     # def get_uri(self,obj):
#     #     return "/api/status/{id}/".format(id=obj.id)

#     def get_uri(self,obj):
#         request = self.context.get("request")
#         return api_reverse("api-user:detail",kwargs={"username" : obj.username}, request = request)

class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri  = serializers.SerializerMethodField(read_only = True)
    # user_id = serializers.PrimaryKeyRelatedField(source="user" ,read_only=True)
    # user_id = serializers.HyperlinkedRelatedField(source="user",
    #                                               lookup_field = "username",
    #                                               view_name="api-user:detail",
    #                                               read_only=True)

    # username = serializers.SlugRelatedField(source = "user" ,read_only=True, slug_field="username")


    class Meta:
        model = Status
        fields =[
            "uri",
            "id",
            "user",
            "content",
            "image",
            # "user_id",
            # "username"
        ]
        read_only_fields = ["user"]

    # def get_uri(self,obj):
    #     return "/api/status/{id}/".format(id=obj.id)
    # def get_user(self,obj):
    #     request = self.context.get("request")
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context = {"request": request}).data
    
    def get_uri(self,obj):
        request = self.context.get("request")
        return api_reverse("api-status:detail",kwargs={"id" : obj.id}, request = request)


    # To validate field name content 
    # validate_<field_name>
    def validate_content(self,value):
        if len(value) > 10000000:
            raise serializers.ValidationError("Content is way too long")
        return value

    # Entire data validation
    def validate(self,data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required")
        return data



class StatusInlineSerializer(StatusSerializer):
    # uri  = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Status
        fields =[
            "uri",
            "id",
            "content",
            "image"
        ]

    # def get_uri(self,obj):
    #     return "/api/status/{id}/".format(id=obj.id)

    # def get_uri(self,obj):
    #     request = self.context.get("request")
    #     return api_reverse("api-user:detail",kwargs={"username" : obj.username}, request = request)