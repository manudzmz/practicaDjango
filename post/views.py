from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
# from django.views import View
import users
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
    posts = Post.objects.all().order_by('-fec_publicacion').select_related("owner")
    context = {'posts_list': posts[:5]}
    return render(request, "post/home.html", context)


def post_detail(request, pk):
    """
    Renderiza el detalle de un post
    :param request: objeto HttpRequest con los datos de la peticion
    :param pk: clave primaria del post a recuperar
    :return:
    """
    possible_posts = Post.objects.filter(pk=pk).select_related("owner")
    if len(possible_posts) == 0:
        return HttpResponseNotFound("El post solicitado no existe")
    elif len(possible_posts) > 1:
        return HttpResponse("Multiples opciones", status=300)

    post = possible_posts[0]
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)


def user_posts(request, blogger):
    """
    Muestra la lista de posts del blog de un usuario
    :param request: objeto HttpRequest con los datos de la peticion
    :param blogger: nombre de usuario de la persona cuyo blog queremos ver
    :return:
    """
    posts_list = Post.objects.all().order_by('-fec_publicacion').select_related("owner")
    context = {"posts_list": posts_list}
    return render(request, 'post/user_posts.html', context)

