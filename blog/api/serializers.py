from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Post, Category, Tag, Comment, CommentReply, Image


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'description']


# Tag Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


# Image Serializer (for other images in posts)
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'caption']


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    main_image = serializers.ImageField(required=False)
    secondary_image = serializers.ImageField(required=False)
    other_images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'category', 'created_at', 'updated_at', 'tags', 'main_image',
                  'secondary_image', 'other_images']


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Showing the username
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


# CommentReply Serializer
class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Showing the username
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = CommentReply
        fields = ['id', 'user', 'content', 'created_at']


# User Profile Serializer (For updating the user's profile picture)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture']
