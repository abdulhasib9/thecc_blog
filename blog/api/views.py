from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Post, Category, Tag, Comment, CommentReply, User
from .serializers import PostSerializer, CategorySerializer, TagSerializer, CommentSerializer, CommentReplySerializer, \
    UserProfileSerializer


def post_list(request):
    # Fetch all posts from the database
    posts = Post.objects.all()

    # Render the template with the list of posts
    return render(request, 'blog/post_list.html', {'posts': posts})







# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Make sure the user is authenticated


# Tag ViewSet
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


# CommentReply ViewSet
class CommentReplyViewSet(viewsets.ModelViewSet):
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [IsAuthenticated]


# User Profile ViewSet (for updating user profile)
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)  # Only allow updating the logged-in user's profile
