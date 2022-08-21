import requests
from django.shortcuts import render
from rest_framework.response import Response

from core.serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
import json

# Create your views here.
class PostAPIView(APIView):
    # def get(self,request):
    #     posts=Post.object.all()
    #     serializer=PostSerializer(posts,many=True)
    #     return Response(serializer.data)
    def get(self,request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    # def formatPost(self,post):
    #     comments=requests.get('http://127.0.0.1:8001/api/posts/%d/comments'%post.id).json()

    #     return {
    #         'id':post.id,
    #         'title':post.title,
    #         'description':post.description,
    #         'comments':comments

    #     }
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostCommentAPIView(APIView):
    def post(self,request,pk=None):
        print(pk)
        post=Post.objects.get(pk=pk)
        comments=json.loads(post.comments)
        comments.append({
            'text':request.data['text']
        })
        post.comments=json.dumps(comments)
        post.save()
        return Response(PostSerializer(post).data)
       