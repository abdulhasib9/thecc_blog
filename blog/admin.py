from django.contrib import admin
from .models import Category, SubCategory, Tag, Post, Comment, CommentReply, Image, Subject, Lesson, CodeSnippet
from django.utils.text import slugify


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'description', 'slug')  # Fields to display in the list view
    search_fields = ('title', 'category__name', 'subcategory__name')  # Fields to use in the search bar
    prepopulated_fields = {'slug': ('title',)}  # Prepopulate slug field based on title


# Admin interface customization for Lesson model
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'order')  # Fields to display in the list view
    search_fields = ('title', 'subject__title')  # Fields to use in the search bar
    list_filter = ('subject',)  # Filters to use in the list view
    ordering = ('order',)  # Order lessons by their 'order' field


# Admin interface customization for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_preview')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to use in the search bar

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else 'No Image'

    image_preview.allow_tags = True  # Allow HTML tags in image preview
    image_preview.short_description = 'Image'  # Short description for the image preview column


# Admin interface customization for SubCategory model
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image_preview')  # Fields to display in the list view
    search_fields = ('name', 'category__name')  # Fields to use in the search bar, including related category name

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else 'No Image'

    image_preview.allow_tags = True  # Allow HTML tags in image preview
    image_preview.short_description = 'Image'  # Short description for the image preview column


# Admin interface customization for Tag model
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Fields to display in the list view
    search_fields = ('name',)  # Fields to use in the search bar


# Admin interface customization for Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'created_at', 'updated_at', 'slug',
                    'main_image_preview')  # Fields to display in the list view
    list_filter = ('category', 'subcategory', 'tags')  # Filters to use in the list view
    search_fields = ('title', 'content')  # Fields to use in the search bar
    prepopulated_fields = {'slug': ('title',)}  # Prepopulate slug field based on title
    filter_horizontal = ('tags', 'other_images', 'code_snippets')  # Horizontal filter for tags, images, and code snippets

    def main_image_preview(self, obj):
        return f'<img src="{obj.main_image.url}" width="50" />' if obj.main_image else 'No Image'

    main_image_preview.allow_tags = True  # Allow HTML tags in image preview
    main_image_preview.short_description = 'Main Image'  # Short description for the main image preview column


# Admin interface customization for Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'content_preview')  # Fields to display in the list view
    search_fields = ('user', 'post', 'content')  # Fields to use in the search bar

    def content_preview(self, obj):
        return obj.content[:50]  # Show only the first 50 characters for preview


# Admin interface customization for CommentReply model
class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at', 'content_preview')  # Fields to display in the list view
    search_fields = ('user', 'content')  # Fields to use in the search bar

    def content_preview(self, obj):
        return obj.content[:50]  # Show only the first 50 characters for preview


# Admin interface customization for Image model
class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image_preview', 'post', 'lesson')  # Fields to display in the list view
    search_fields = ('caption',)  # Fields to use in the search bar
    list_filter = ('post', 'lesson')  # Filters to use in the list view

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else 'No Image'

    image_preview.allow_tags = True  # Allow HTML tags in image preview
    image_preview.short_description = 'Image'  # Short description for the image preview column


# Admin interface customization for CodeSnippet model
class CodeSnippetAdmin(admin.ModelAdmin):
    list_display = ('language', 'description', 'post', 'lesson')  # Fields to display in the list view
    search_fields = ('language', 'description')  # Fields to use in the search bar
    list_filter = ('language',)  # Filters to use in the list view


# Registering the models with custom admin views
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CodeSnippet, CodeSnippetAdmin)
