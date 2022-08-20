import requests
from django.shortcuts import render
from rest_framework.response import Response

from core.serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView

# Create your views here.
class PostAPIView(APIView):
    # def get(self,request):
    #     posts=Post.object.all()
    #     serializer=PostSerializer(posts,many=True)
    #     return Response(serializer.data)
    def get(self,request):
        posts=Post.object.all()
        return Response()
    def formatPost(self,post):
        comments=requests.get('http://127.0.0.1:8001/api/posts/%d/comments'%post.id).json()

        return {
            'id':post.id,
            'title':post.title,
            'description':post.description,
            'comments':comments

        }
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

