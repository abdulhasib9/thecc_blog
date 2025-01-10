from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    """
    Represents a category for blog posts with an image.
    """
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to="category_images/")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Represents a tag that can be associated with a post.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post with a slug, multiple images, and tags.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Slug for the URL
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    main_image = models.ImageField(upload_to="post_images/main/", null=True, blank=True)
    secondary_image = models.ImageField(upload_to="post_images/secondary/", null=True, blank=True)
    other_images = models.ManyToManyField('Image', related_name="posts", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


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


class Image(models.Model):
    """
    Represents an image that can be associated with a post.
    """
    image = models.ImageField(upload_to="post_images/other/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image - {self.caption if self.caption else 'No Caption'}"
