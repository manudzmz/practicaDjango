from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)  # authenticate solo recupera el usuario de la BD
        if user is None:
            error_message = "Usuario o contraseña incorrecto"
        else:
            if user.is_active:
                django_login(request, user)  # Le "asigna" al objeto request el usuario autenticado
                return redirect("/")
            else:
                error_message = "Cuenta de usuario inactiva"

    return render(request, "users/login.html", {"error": error_message})


def logout(request):
    """
    Hace el logout de un usuario y redirige al login
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    if request.user.is_authenticated():
        django_logout(request)
    return redirect("/")


def blogs(request):
    """
    Muestra la lista de usuarios que tienen blog en la plataforma
    :param request: objeto HttpRequest con los datos de la peticion
    :return:
    """
    bloggers_list = User.objects.all()
    context = {"bloggers": bloggers_list}
    return render(request, "users/blogs.html", context)