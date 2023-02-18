from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.code}, {self.name}"

    class Meta:
        verbose_name_plural = "County Entries"
    

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"Address: {self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # One-to-One
    address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)


    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()
        

class Book(models.Model):
    bookName = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # Foreign Key to setup one-to-many relationship
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE) 

    is_bestselling = models.BooleanField(default=False)
    release_year = models.DateField(default=timezone.now())
    slug = models.SlugField(default="", null=False)

    # Many-to-Many relationship
    published_country = models.ManyToManyField(Country)

    def __str__(self):
        return f"Title:{self.bookName} Rating:({self.rating}) Author: {self.author} Release:{self.release_year}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    




