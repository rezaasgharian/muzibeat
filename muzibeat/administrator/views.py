from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def Posts(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'administrator/posts.html', context)