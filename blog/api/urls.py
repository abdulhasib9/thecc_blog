from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, TagViewSet, PostViewSet, CommentViewSet, CommentReplyViewSet, UserProfileViewSet, LessonViewSet, CodeSnippetViewSet
from . import views

# Initialize the router and register the viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)  # Register SubCategoryViewSet
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'replies', CommentReplyViewSet)
router.register(r'user-profile', UserProfileViewSet)
router.register(r'lessons', LessonViewSet)  # Register LessonViewSet
router.register(r'code-snippets', CodeSnippetViewSet)  # Register CodeSnippetViewSet

urlpatterns = [
    path('api/', include(router.urls)),  # Base API path
    path('test/', views.post_list, name='post_list'),
]
