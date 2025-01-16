from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    """
    Represents a category for subjects and posts.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # Add image field
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    """
    Represents a subcategory that belongs to a category.
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)  # Add image field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subject(models.Model):
    """
    Represents a subject that belongs to a category.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subjects")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subjects", blank=True, null=True)  # Optional subcategory field
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContentBlock(models.Model):
    """
    Represents a content block that can be used in lessons or posts (text, images, code snippets).
    """
    TEXT = 'text'
    IMAGE = 'image'
    CODE = 'code'
    CONTENT_TYPES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
        (CODE, 'Code Snippet'),
    ]

    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    content = models.TextField(blank=True, null=True)  # For text and code content
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)  # For image content
    code_language = models.CharField(max_length=50, blank=True, null=True)  # For code content (e.g., Python)
    order = models.IntegerField(default=0)  # To control the order of content blocks

    def __str__(self):
        return f"Content Block: {self.content_type} - Order: {self.order}"


class Lesson(models.Model):
    """
    Represents a lesson within a subject.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    order = models.IntegerField()
    content_blocks = models.ManyToManyField(ContentBlock, related_name="lessons", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}. {self.title}"


class Post(models.Model):
    """
    Represents a blog post that can be linked to a category and have multiple content blocks.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()  # Main content for the post (optional since we use content blocks)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_blocks = models.ManyToManyField(ContentBlock, related_name="posts", blank=True)
    main_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    secondary_image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    Represents a tag that can be associated with a post.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    Represents a comment on a post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class CommentReply(models.Model):
    """
    Represents a reply to a comment.
    """
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.user.username} on Comment ID {self.comment.id}"


class Menu(models.Model):
    """
    Represents a menu that contains multiple menu items.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Menu(models.Model):
    """
    Represents a menu, which can have multiple menu items.
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Represents a menu item, which can be a top-level menu item or a sub-menu item.
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_menu_items', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return self.title





# class Menu(models.Model):
#     """
#     Represents a navigation menu.
#     """
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, blank=True)
#     description = models.TextField(blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Menu, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
#
# class MenuItem(models.Model):
#     """
#     Represents an item in a navigation menu.
#     """
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menu_items")
#     title = models.CharField(max_length=255)
#     link = models.CharField(max_length=200)
#     order = models.IntegerField(default=0)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_items", blank=True, null=True)
#
#     def __str__(self):
#         return self.title
