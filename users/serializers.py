from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile

BLOG_URL = "http://127.0.0.1:8000/blogs/"


class BlogsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Profile

    def get_url(self, user):
        url = BLOG_URL
        complete_url = url + str(user.username)
        return complete_url


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = make_password(validated_data.get('password'))
        instance.save()
        return instance