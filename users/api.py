from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,  HTTP_202_ACCEPTED, \
    HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from users.permissions import UserPermission
from users.serializers import BlogsSerializer, UserSerializer


class BlogsListAPI(APIView):
    """
    Endpoint que muestra el listado de blogs de la plataforma
    """
    permission_classes = (UserPermission,)

    def get(self, request):
        users = User.objects.all()
        serializer = BlogsSerializer(users, many=True)
        return Response(serializer.data)


#
# class SignupAPII(APIView):
#     """
#     Endpoint de creación de usuarios
#     """
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class SignupAPI(CreateAPIView):
    """
    Endpoint de creación de usuarios
    """
    permission_classes = (UserPermission,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(APIView):
    """
    Endpoint de detalle de un usuario
    """
    permission_classes = (UserPermission,)

    def get(self, request, blogger):
        user = get_object_or_404(User, username=blogger)
        self.get_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, blogger):
        user = get_object_or_404(User, username=blogger)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, blogger):
        user = get_object_or_404(User, username=blogger)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

# class UserDetailAPI(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     if not queryset:
#         pass
#     serializer_class = UserSerializer

    # def get_queryset(self):
    #     return User.objects.filter(username=self.kwargs["blogger"])


