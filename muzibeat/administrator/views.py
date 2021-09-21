from django.shortcuts import render , get_object_or_404
from .models import Post

# Create your views here.
def Posts(request):
    context = {
        'posts':Post.objects.filter(status = "p").order_by('-publish')  ,
    }
    return render(request, 'administrator/index.html', context)

def detail(request ,slug):
    context = {
        'post':  get_object_or_404(Post , slug=slug , status = "p")
    }
    return render(request , "administrator/posts.html" ,context)