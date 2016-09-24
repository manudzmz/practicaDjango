from rest_framework import serializers

from users.models import Profile

BLOG_URL = "http://127.0.0.1:8000/blogs/"


class BlogsSerializer(serializers.Serializer):
    username = serializers.CharField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Profile

    def get_url(self, user):
        url = BLOG_URL
        complete_url = url + str(user.username)
        return complete_url
