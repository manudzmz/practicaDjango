from django.conf.urls import url
from users.views import LoginView, LogoutView, BlogsView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^blogs/$', BlogsView.as_view()),
]