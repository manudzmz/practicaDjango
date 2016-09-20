from django.shortcuts import render

# Create your views here.
# from django.views import View

from post.models import Post


# class HomeView(View):
#     def get(self, request):
#         """
#         Renderiza el home con un listado de los ultimos post publicados por los usuarios
#         :param request: objeto HttpRequest con los datos de la peticion
#         :return:
#         """
#         posts = Post.objects.order_by('-fec_publicacion')
#         context = {'posts_list': posts[:5]}
#         return render(request, "post/home.html", context)

def home(request):
    """
    Renderiza el home con un listado de los ultimos post publicados por los usuarios
    :param request: objeto HttpRequest con los datos de la peticion
    :return:
    """
    posts = Post.objects.all()
    context = {'posts_list': posts[:5]}
    return render(request, "post/home.html", context)
