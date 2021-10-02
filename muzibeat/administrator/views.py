from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def Posts(request):
    context = {
        'posts':Post.objects.filter(status = "p").order_by('-publish'),
    }
    return render(request, 'administrator/index.html', context)
@login_required(login_url='/login/')
def detail(request ,slug):
    context = {
        'post':  get_object_or_404(Post , slug=slug , status = "p")
    }
    return render(request, "administrator/posts.html",context)