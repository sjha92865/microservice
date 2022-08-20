

from rest_framework.response import Response

from core.serializers import CommentSerializer
from .models import Comment
from rest_framework.views import APIView

# Create your views here.
class PostCommentAPIView(APIView):
    def get(self,_,pk=None):
        comments=Comment.objects.filter(post_id=pk)
        serializer=CommentSerializer(comments,many=True)
        return Response(serializer.data)

        
class CommentsAPIView(APIView):
    

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

