from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from users.serializers import BlogsSerializer, UserSerializer


class BlogsListAPI(APIView):
    """
    Endpoint que muestra el listado de blogs de la plataforma
    """

    def get(self, request):
        users = User.objects.all()
        serializer = BlogsSerializer(users, many=True)
        return Response(serializer.data)


class SignupAPI(APIView):
    """
    Endpoint de creación de usuarios
    """

    def post(self, request):
        serializer = UserSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    """
    Endpoint de detalle de un usuario
    """

    def get(self, request, blogger):
        # blogger = self.kwargs["blogger"]
        # user = get_object_or_404(User, user__username=blogger)
        # serializer = UserSerializer(user)
        # if request.user == blogger:
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)

        # blogger = self.kwargs["blogger"]
        user = get_object_or_404(User, username=blogger)
        serializer = UserSerializer(user)
        return Response(serializer.data)

