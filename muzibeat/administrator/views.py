from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, category
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def Posts(request):
    context = {
        'posts': Post.objects.filter(status="p").order_by('-publish'),
        "category": category.objects.filter(status=True)
    }
    return render(request, 'administrator/index.html', context)


@login_required(login_url='/login/')
def detail(request, slug):
    context = {
        'post': get_object_or_404(Post, slug=slug, status="p"),
        "category": category.objects.filter(status=True)
    }
    return render(request, "administrator/posts.html", context)


def categry(requests, slug):
    context = {
        'cate': get_object_or_404(category, slug=slug, status=True)
    }
    return render(requests, "administrator/category.html", context)
