from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubjectViewSet, ContentBlockViewSet, LessonViewSet, PostViewSet, TagViewSet, CommentViewSet, CommentReplyViewSet, MenuViewSet, MenuItemViewSet, get_menu_with_items, get_menu_items

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'content-blocks', ContentBlockViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'comment-replies', CommentReplyViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/menus/<slug:menu_slug>/items/', get_menu_items, name='get_menu_items'),
    path('api/menus/<slug:menu_slug>/', get_menu_with_items, name='get_menu_with_items'),
]
