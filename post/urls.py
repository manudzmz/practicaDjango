from django.conf.urls import url
from django.contrib import admin

from post.views import home, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^blogs/usuario/(?P<pk>[0-9]+)$', post_detail),
]