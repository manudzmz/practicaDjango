from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import BlogsSerializer


class BlogsListAPI(APIView):
    """
    Endpoint que muestra el listado de blogs de la plataforma
    """

    def get(self, request):
        users = User.objects.all()
        serializer = BlogsSerializer(users, many=True)
        return Response(serializer.data)
