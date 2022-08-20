

from rest_framework.response import Response

from core.serializers import CommentSerializer

from rest_framework.views import APIView

# Create your views here.
class CommentsAPIView(APIView):
    

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

