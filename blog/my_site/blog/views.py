from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post, Author, Tag


def get_date(post):
    return post['date']

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tag.all()
    })
