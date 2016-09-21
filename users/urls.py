from django.conf.urls import url
from users.views import login, logout, blogs

urlpatterns = [
    url(r'^login$', login),
    url(r'^logout$', logout),
    url(r'^blogs/$', blogs),
]