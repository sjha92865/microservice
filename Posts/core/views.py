import re
from django.shortcuts import render
from rest_framework.response import Response

from core.serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView

# Create your views here.
class PostAPIView(APIView):
    def get(self,request):
        posts=Post.object.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

