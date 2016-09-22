from django.conf.urls import url
from django.contrib import admin

from post.views import HomeView, PostDetailView, user_posts, CreatePostView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', user_posts),
    url(r'^blogs/[a-z0-9_-]+/(?P<pk>[0-9]+)$', PostDetailView.as_view()),
    url(r'^new-post$', CreatePostView.as_view()),
]