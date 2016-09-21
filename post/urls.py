from django.conf.urls import url
from django.contrib import admin

from post.views import home, post_detail, user_posts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', user_posts),
    url(r'^blogs/[a-z0-9_-]+/(?P<pk>[0-9]+)$', post_detail),
]