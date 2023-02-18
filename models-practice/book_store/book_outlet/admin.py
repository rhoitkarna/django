from django.contrib import admin
from .models import Book, Author, Address, Country

# Register Models here
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("bookName",)
    }
    list_filter = ("rating", "author")
    list_display = ("bookName","author")
    

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)