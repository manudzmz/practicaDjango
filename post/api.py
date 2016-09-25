from django.db.models import Q
from django.utils.datetime_safe import datetime
from rest_framework import filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from post.models import Post
from post.permissions import PostDetailPermission
from post.serializers import UserPostsSerializer, UserPostsListsSerializer


class UserPostsAPI(ListAPIView):
    """
    Endpoint que muestra la lista de posts en el blog de un usuario
    """
    queryset = Post.objects.all()
    serializer_class = UserPostsListsSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = ('titulo', 'fec_publicacion')
    search_fields = ('titulo', 'cuerpo')

    def list(self, request, blogger):
        if request.user.is_authenticated and (request.user.username == blogger or request.user.is_superuser):
            queryset = self.get_queryset().filter(owner__username=blogger).order_by(
                '-fec_publicacion')
        else:
            queryset = self.get_queryset().filter(
                Q(owner__username=blogger) & Q(fec_publicacion__lte=datetime.now())).order_by(
                '-fec_publicacion')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Endpoint de detalle del post de un usuario
    """
    queryset = Post.objects.all()
    serializer_class = UserPostsSerializer
    permission_classes = (PostDetailPermission,)

    def retrieve(self, request, pk, blogger):
        post = get_object_or_404(Post, pk=pk, owner__username=blogger)
        self.check_object_permissions(request, post)
        serializer = UserPostsSerializer(post)
        return Response(serializer.data)

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            return serializer.save(owner=self.request.user)
        else:
            return serializer.save()


class CreatePostAPI(CreateAPIView):
    """
    Endpoint de creación de un nuevo post (solo usuarios autenticados)
    """
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = UserPostsSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
