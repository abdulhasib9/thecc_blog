# myapp/serializers.py
from rest_framework import serializers
from ..models import Category, Subject, ContentBlock, Lesson, Post, Tag, Comment, CommentReply, Menu, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class SubjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Category Serializer
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug', 'category', 'description']


class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ['id', 'content_type', 'content', 'image', 'code_language', 'order']


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()  # Nested Subject Serializer
    content_blocks = ContentBlockSerializer(many=True)  # Nested ContentBlock Serializer
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'subject', 'order', 'content_blocks']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested Category Serializer
    content_blocks = ContentBlockSerializer(many=True)  # Nested ContentBlock Serializer
    main_image = serializers.ImageField(required=False)
    secondary_image = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'category', 'created_at', 'updated_at', 'content_blocks', 'main_image', 'secondary_image']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of user ID
    post = PostSerializer()  # Nested Post Serializer

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']


class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of user ID
    comment = CommentSerializer()  # Nested Comment Serializer

    class Meta:
        model = CommentReply
        fields = ['id', 'comment', 'user', 'content', 'created_at']



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'menu', 'parent', 'url', 'order']

class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'slug', 'menu_items']
