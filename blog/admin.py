from django.contrib import admin
from .models import Category, Tag, Post, Comment, CommentReply, Image
from django.utils.text import slugify


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_preview')
    search_fields = ('name',)

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'slug', 'main_image_preview')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)

    def main_image_preview(self, obj):
        return f'<img src="{obj.main_image.url}" width="50" />' if obj.main_image else 'No Image'

    main_image_preview.allow_tags = True
    main_image_preview.short_description = 'Main Image'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'content_preview')
    search_fields = ('user', 'post', 'content')

    def content_preview(self, obj):
        return obj.content[:50]  # Show only the first 50 characters for preview


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at', 'content_preview')
    search_fields = ('user', 'content')

    def content_preview(self, obj):
        return obj.content[:50]  # Show only the first 50 characters for preview


class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image_preview', 'post')
    search_fields = ('caption',)
    list_filter = ('post',)

    def image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="50" />' if obj.image else 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Image'


# Registering the models with custom admin views
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(Image, ImageAdmin)
