from rest_framework import serializers

from post.models import Post


class UserPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post

