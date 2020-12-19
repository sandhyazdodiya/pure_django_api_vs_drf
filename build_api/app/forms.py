from django import forms
from app.models import Update


class UpdateModelForm(forms.UpdateModelForm):
    class Meta:
        model = Update
        fields = [
            "user",
            "content",
            "image",
        ]
