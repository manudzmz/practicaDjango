from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework.renderers import JSONRenderer

from users.serializers import BlogsSerializer


class BlogsListAPI(View):
    """
    Endpoint que muestra el listado de blogs de la plataforma
    """

    def get(self, request):
        users = User.objects.all()
        serializer = BlogsSerializer(users, many=True)
        renderer = JSONRenderer()
        data = renderer.render(serializer.data)
        return HttpResponse(data)
