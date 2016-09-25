from django.db.models import Q
from django.utils.datetime_safe import datetime
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from post.models import Post
from post.serializers import UserPostsSerializer, UserPostsListsSerializer


class UserPostsAPI(ListAPIView):
    """
    Endpoint que muestra la lista de posts en el blog de un usuario
    """

    queryset = Post.objects.all()
    serializer_class = UserPostsListsSerializer

    def list(self, request, blogger):
        if request.user.is_authenticated and (request.user.username == blogger or request.user.is_superuser):
            queryset = self.get_queryset().filter(owner__username=blogger).order_by(
                '-fec_publicacion')
        else:
            queryset = self.get_queryset().filter(
                Q(owner__username=blogger) & Q(fec_publicacion__lte=datetime.now())).order_by(
                '-fec_publicacion')

        # serializer = UserPostsSerializer(queryset, many=True)
        # return Response(serializer.data)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
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
        instance = get_object_or_404(queryset)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
