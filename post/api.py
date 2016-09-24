from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


# class UserPostsAPI(APIView):
#     """
#     Endpoint que muestra el detalle de un usuario con su lista de posts
#     """
#
#     def get(self, request):
#         user = get_object_or_404(User, user__username=self.kwargs["blogger"])
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
