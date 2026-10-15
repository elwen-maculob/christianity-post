from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Publish")
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, related_name='posts')
    content = models.TextField()
    verse_highlight = models.TextField(blank=True, null=True, help_text="Optional scripture verse to meditate on.")
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    created_on = models.DateField()
    updated_on = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False, help_text="Check this box to feature this post on the homepage.")

class Meta:
        ordering = ['-created_on']

def __str__(self):
        return self.title