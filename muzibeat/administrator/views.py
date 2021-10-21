from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url='/login/')
def Post_admin(request):
    if request.method == 'POST':
        if not request.POST['title'] or len(request.POST['title'])<3:
            raise ValueError("title must be valid")
        if not request.POST['des'] or len(request.POST['des'])<3:
            raise ValueError("description must be valid")
        post = Post.objects.create(user_id=request.user.user_id,title=request.POST['title'],description=request.POST['des'])
        img = Images.objects.create(post_id=post.id, thumbnail=request.FILES['thumbnail'])
        video = Videos.objects.create(post_id=post.id, file=request.FILES['video'])
        voice = Voices.objects.create(post_id=post.id, file=request.FILES['voice'])
        file = Files.objects.create(post_id=post.id, file=request.FILES['file'])
        post.save()
        img.save()
        video.save()
        voice.save()
        file.save()
    return render(request, 'account/admin_create_post.html')


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