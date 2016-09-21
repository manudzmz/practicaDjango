from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from users.forms import LoginForm


def login(request):
    """
    Presenta el formulario de login y gestiona el login de un usuario
    :param request: objeto HttpRequest con los datos de la petición
    :return: objeto HttpResponse con los datos de la respuesta
    """
    error_message = ""
    login_form = LoginForm(request.POST) if request.method == "POST" else LoginForm()
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("pwd")
            user = authenticate(username=username, password=password)  # authenticate solo recupera el usuario de la BD
            if user is None:
                error_message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)  # Le "asigna" al objeto request el usuario autenticado
                    return redirect(request.GET.get("next", "/"))
                else:
                    error_message = "Cuenta de usuario inactiva"

    context = {"error": error_message, "form": login_form}
    return render(request, "users/login.html", context)


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
