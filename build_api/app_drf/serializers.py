from rest_framework import serializers
from app_drf.models import Status
from accounts.serializers import UserPublicSerializer
"""
Serializer ---> Converts to Json
Serializer ---> Validates data
"""

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


class StatusInlineSerializer(serializers.ModelSerializer):
    uri  = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Status
        fields =[
            "uri",
            "id",
            "content",
            "image"
        ]

    def get_uri(self,obj):
        return "/api/status/{id}/".format(id=obj.id)


class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri  = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Status
        fields =[
            "uri",
            "id",
            "user",
            "content",
            "image"
        ]
        read_only_fields = ["user"]

    def get_uri(self,obj):
        return "/api/status/{id}/".format(id=obj.id)


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