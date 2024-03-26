from django.db import models
from user_profile.models import User
from django.utils.text import slugify

# Create your models here.

############################ Category ##############################


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


############################ Tag ##############################
class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

############################ Blog ##############################


class Blog(models.Model):
    user = models.ForeignKey(
        User, related_name='user_blogs', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='category_blogs', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tag_blogs')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=300)
    banner = models.ImageField(upload_to="blog_Images",)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

############################ Comment ##############################


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='user_comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(
        Blog, related_name='blog_comments', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

############################ Reply ##############################


class Reply(models.Model):
    user = models.ForeignKey(
        User, related_name='user_Replies', on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='comment_Replies', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
