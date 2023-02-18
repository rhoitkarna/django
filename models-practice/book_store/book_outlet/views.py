from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    book = Book.objects.all().order_by("bookName")
    count = book.count()
    avg_rating = book.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", context={
        "books": book,
        "count": count,
        "avg_rating": avg_rating
    })
    
def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    context = {
        "name": book.bookName,
        "rating": book.rating,
        "author": book.author,
        "release": book.release_year,
        "bs": book.is_bestselling
    }
    return render(request, "book_outlet/book_details.html", context=context)