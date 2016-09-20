from django.conf.urls import url, include

from post.views import HomeView

urlpatterns = [
    # Web URLs
    url(r'^$', HomeView.as_view(), name='posts_home'),

    # API URLs
    # url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='api_photos_list'),
    # url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='api_photos_detail'),
    #url(r'', include(router.urls)),
]