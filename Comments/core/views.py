

from rest_framework.response import Response

from core.serializers import CommentSerializer
from .models import Comment
from rest_framework.views import APIView
import requests
import random
# Create your views here.
class PostCommentAPIView(APIView):
    def get(self,_,pk=None):
        comments=Comment.objects.filter(post_id=pk)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)


class CommentsAPIView(APIView):
    

    def post(self,request):
        serializer=CommentSerializer(data=request.data)#3rd comment me kadbad ho gya, replace with CommentSerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        comment=serializer.data

        if random.randint(1,10)<=9:


            r=requests.post('http://127.0.0.1:8000/api/posts/%d/comments'%comment['post_id'],data={
                    'text':comment['text']
            })
            if not r.ok:
                pass


        return Response(serializer.data)

