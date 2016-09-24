from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import UserPostsSerializer
from rest_framework.status import HTTP_404_NOT_FOUND


class UserPostsAPI(ListAPIView):
    """
    Endpoint que muestra la lista de posts en el blog de un usuario
    """

    queryset = Post.objects.all()
    serializer_class = UserPostsSerializer

    def list(self, request, blogger):
        queryset = self.get_queryset().filter(owner__username=blogger).order_by(
            '-fec_publicacion')
        serializer = UserPostsSerializer(queryset, many=True)
        return Response(serializer.data)

        # def get(self, request):
        #     user = get_object_or_404(User, user__username=self.kwargs["blogger"])
        #     serializer = UserSerializer(user)
        #     return Response(serializer.data)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UserPostsSerializer

    def retrieve(self, request, pk, blogger):
        queryset = self.get_queryset().filter(Q(pk=pk) & Q(owner__username=blogger))
        serializer = UserPostsSerializer(queryset, many=True)
        if not serializer.data:
            return Response(status=HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data)
