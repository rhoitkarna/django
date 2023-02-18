from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


# Tag Model
class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

# Author Model
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


# Post Model 
class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    slug = models.SlugField(unique=True, null=False, db_index=True)
    content = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("post-detail-page", kwargs={"slug":self.slug})
    


