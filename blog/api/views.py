from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Category, Subject, ContentBlock, Lesson, Post, Tag, Comment, CommentReply, Menu, MenuItem
from .serializers import CategorySerializer, SubjectSerializer, ContentBlockSerializer, LessonSerializer, PostSerializer, TagSerializer, CommentSerializer, CommentReplySerializer, MenuSerializer, MenuItemSerializer

# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Subject ViewSet
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
# ContentBlock ViewSet
class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

# Lesson ViewSet
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Tag ViewSet
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# CommentReply ViewSet
class CommentReplyViewSet(viewsets.ModelViewSet):
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer

# Menu ViewSet
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# MenuItem ViewSet
# views.py


class MenuViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Menu instances.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing MenuItem instances.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view(['GET'])
def get_menu_with_items(request, menu_slug):
    """
    Fetch the menu by its slug and return the menu along with its menu items.
    """
    try:
        menu = Menu.objects.get(slug=menu_slug)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    except Menu.DoesNotExist:
        return Response({"error": "Menu not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_menu_items(request, menu_slug):
    """
    Fetch the menu items for a specific menu identified by its slug.
    """
    try:
        menu = Menu.objects.get(slug=menu_slug)
        menu_items = menu.menu_items.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
    except Menu.DoesNotExist:
        return Response({"error": "Menu not found"}, status=status.HTTP_404_NOT_FOUND)
