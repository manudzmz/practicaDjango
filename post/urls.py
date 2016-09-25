from django.conf.urls import url

from post.api import UserPostsAPI, CreatePostAPI, PostDetailAPI
from post.views import HomeView, PostDetailView, UserPostsView, CreatePostView


urlpatterns = [
    #Web URLs
    url(r'^$', HomeView.as_view(), name='post_home'),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/$', UserPostsView.as_view(), name='post_usersposts'),
    url(r'^blogs/(?P<blogger>[a-z0-9_-]+)/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_postdetail'),
    url(r'^new-post$', CreatePostView.as_view(), name='post_createpost'),

    #API URLs
    url(r'^api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)/$', UserPostsAPI.as_view(), name='api_usersposts'),
    url(r'^api/1.0/blogs/(?P<blogger>[a-z0-9_-]+)/(?P<pk>[0-9]+)$', PostDetailAPI.as_view(), name='api_postdetail'),
    url(r'^api/1.0/new-post$', CreatePostAPI.as_view(), name='api_newpost'),
]