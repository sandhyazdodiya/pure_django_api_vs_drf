from rest_framework import serializers
from app_drf.models import Status

"""
Serializer ---> Converts to Json
Serializer ---> Validates data
"""

class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()




class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields =[
            "id",
            "user",
            "content",
            "image"
        ]
        read_only_fields = ["user"]


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