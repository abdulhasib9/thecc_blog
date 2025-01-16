from django.contrib import admin
from .models import Category, SubCategory, Subject, ContentBlock, Lesson, Post, Tag, Comment, CommentReply, Menu, MenuItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('category', 'subcategory')
    prepopulated_fields = {'slug': ('title',)}


class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'order')
    search_fields = ('content_type',)
    list_filter = ('content_type',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'order')
    search_fields = ('title',)
    list_filter = ('subject',)
    ordering = ('order',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'main_image', 'secondary_image')
    search_fields = ('title',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username')
    list_filter = ('post', 'user')


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'created_at')
    search_fields = ('comment__id', 'user__username')
    list_filter = ('comment', 'user')


# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     search_fields = ('name',)
#     prepopulated_fields = {'slug': ('name',)}


# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ('menu', 'title', 'link', 'order', 'parent')
#     search_fields = ('title',)
#     list_filter = ('menu', 'parent')

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1  # Number of empty rows to display in the inline form
    fields = ['title', 'slug', 'parent', 'url', 'order', 'image']
    readonly_fields = ['slug']  # Make the slug field read-only

from django.contrib import admin
from .models import Menu, MenuItem

# Admin interface customization for Menu model
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Update to reflect available fields
    search_fields = ('name',)

# Admin interface customization for MenuItem model
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'url', 'order')  # Update to reflect available fields
    search_fields = ('title', 'menu__name', 'parent__title')
    list_filter = ('menu', 'parent')
    ordering = ('menu', 'order')

# Registering the models with custom admin views



# Register models with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
