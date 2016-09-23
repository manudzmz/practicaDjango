from django.conf.urls import url
from users.views import LoginView, LogoutView, BlogsView, SignupView

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^signup$', SignupView.as_view(), name='users_signup'),
    url(r'^blogs/$', BlogsView.as_view(), name='users_blogs'),
]