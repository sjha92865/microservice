

from rest_framework import serializers
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"
    