from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Menu(models.Model):
    """
    Represents a menu that contains multiple menu items.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Represents a menu item, which can be a top-level menu item or a sub-menu item.
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_menu_items', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# Model to represent a Category for blog posts
class Category(models.Model):
    """
    Represents a category for blog posts with an image.
    """
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="category_images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Model to represent a SubCategory belonging to a Category
class SubCategory(models.Model):
    """
    Represents a subcategory for blog posts that belongs to a category.
    """
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    image = models.ImageField(upload_to="subcategory_images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


# Model to represent a Subject that belongs to either a Category or a SubCategory
class Subject(models.Model):
    """
    Represents a subject that can belong to either a category or a subcategory.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subjects", blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subjects", blank=True,
                                    null=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# Model to represent a Lesson within a Subject
class Lesson(models.Model):
    """
    Represents a lesson within a subject.
    """
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="lessons")
    content = models.TextField()
    order = models.IntegerField()
    urls = models.JSONField(blank=True, null=True)  # To store multiple URLs as a JSON array
    images = models.ManyToManyField('Image', related_name="lessons", blank=True)  # Linking to the Image model
    code_snippets = models.ManyToManyField('CodeSnippet', related_name="lessons",
                                           blank=True)  # Linking to the CodeSnippet model

    def __str__(self):
        return f"{self.order}. {self.title}"


# Model to represent a Tag that can be associated with a Post
class Tag(models.Model):
    """
    Represents a tag that can be associated with a post.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Model to represent a Blog Post
class Post(models.Model):
    """
    Represents a blog post with a slug, multiple images, and tags.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Slug for the URL
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    main_image = models.ImageField(upload_to='post_images/main/', null=True, blank=True)
    secondary_image = models.ImageField(upload_to='post_images/secondary/', null=True, blank=True)
    other_images = models.ManyToManyField('Image', related_name="posts", blank=True)  # Linking to the Image model
    urls = models.JSONField(blank=True, null=True)  # To store multiple URLs as a JSON array
    code_snippets = models.ManyToManyField('CodeSnippet', related_name="posts",
                                           blank=True)  # Linking to the CodeSnippet model

    def image_upload_to(self, filename):
        # Generate dynamic upload path based on the post title
        title_prefix = slugify(self.title)  # Slugify title for a safe file name
        return f"post_images/{title_prefix}/{filename}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate a slug from the title

        # Update the upload_to for images based on the post title
        if self.main_image:
            self.main_image.upload_to = self.image_upload_to(self.main_image.name)
        if self.secondary_image:
            self.secondary_image.upload_to = self.image_upload_to(self.secondary_image.name)

        # Saving the post
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# Model to represent a Comment on a Post
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


# Model to represent a Reply to a Comment
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


# Model to represent an Image that can be associated with a Post or Lesson
class Image(models.Model):
    """
    Represents an image that can be associated with a post or lesson.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_images", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_images", blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    caption = models.CharField(max_length=255, blank=True)

    def image_upload_to(self, filename):
        # Generate dynamic upload path based on the associated post's title
        title_prefix = slugify(
            self.post.title if self.post else self.lesson.title)  # Slugify title for a safe file name
        return f"post_images/{title_prefix}/{filename}"

    def save(self, *args, **kwargs):
        # Update the upload_to for images based on the associated post or lesson title
        if self.image:
            self.image.upload_to = self.image_upload_to(self.image.name)
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return f"Image - {self.caption if self.caption else 'No Caption'}"


# Model to represent a Code Snippet that can be associated with a Post or Lesson
class CodeSnippet(models.Model):
    """
    Represents a code snippet that can be associated with a post or lesson.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_code_snippets", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_code_snippets", blank=True,
                               null=True)
    code = models.TextField()
    language = models.CharField(max_length=50)  # Language of the code snippet (e.g., 'Python', 'JavaScript')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"CodeSnippet in {self.language} - {self.description[:30]}..." if self.description else f"CodeSnippet in {self.language}"
