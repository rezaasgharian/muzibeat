from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.views.decorators.http import require_POST
from django.views.generic.edit import UpdateView, DeleteView
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from matplotlib.image import thumbnail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shortuuidfield import ShortUUIDField
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.forms import modelformset_factory
from django.urls import reverse_lazy


# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('account:profile')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account:profile")
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "account/login.html", context)
    else:
        return render(request, 'account/login.html', {})


def Register(request):
    if request.user.is_authenticated:
        return redirect('account:profile')
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'],
                                            password=data['password_Confirmation'])
            user.save()
            return redirect('account:login')

    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required(login_url='/login/')
def Logout_view(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='/login/')
def Profiles(request):
    posts = Post_user.objects.filter(user_id = request.user.user_id)
    context = {
        'profile': Profile.objects.get(user_id=request.user.user_id),
        'posts':posts,
        'user':request.user.user_id
    }
    return render(request, 'account/profile.html', context)


@login_required(login_url='/login/')
def Post_users(request):
    if request.method == 'POST':
        if not request.POST['title'] or len(request.POST['title']) < 3:
            raise ValueError("title must be valid")
        if not request.POST['des'] or len(request.POST['des']) < 3:
            raise ValueError("description must be valid")
        post = Post_user.objects.create(user_id=request.user.user_id, title=request.POST['title'],
                                        description=request.POST['des'])
        post.save()

        if request.POST['category']:
            print(request.POST['category'])
            cate = Category_user.objects.create(title=request.POST['category'], post_id=post.id)
            cate.save()

        if request.FILES.get('thumbnail', False):
            images = request.FILES.getlist('thumbnail')
            count = len(images)
            if count > 10:
                raise ValidationError('please enter > 10')
            for cnt in range(int(count)):
                ext = os.path.splitext(str(images[cnt]))[1]
                print(ext)
                valid_extensions = ['.jpg', '.jpeg', '.png']
                if not ext.lower() in valid_extensions:
                    raise ValidationError('Unsupported file extension`.')
            for image in images:
                img = Images.objects.create(post_id=post.id, thumbnail=image)
                img.save()

        if request.FILES.get('video', False):
            vid = request.FILES['video'].name
            ext = os.path.splitext(vid)[1]
            valid_extensions = ['.mp4', '.mkv', '.mov', '.wmv']
            if ext.lower() in valid_extensions:
                filename = os.path.splitext(vid)[0] + '.mp4'
                video = Videos.objects.create(post_id=post.id, file=filename)
                video.save()
            else:
                raise ValidationError('Unsupported file extension.')

        if request.FILES.get('voice', False):
            voc = request.FILES['voice'].name
            ext = os.path.splitext(voc)[1]
            valid_extensions = ['.mp3', '.aac']
            if not ext.lower() in valid_extensions:
                filename = os.path.splitext(voc)[0] + '.ogg'
                voice = Voices.objects.create(post_id=post.id, file=filename)
                voice.save()
            else:
                raise ValidationError('Unsupported file extension.')

        if request.FILES.get('file', False):
            fil = request.FILES['file'].name
            ext = os.path.splitext(fil)[1]
            valid_extensions = ['.pdf']
            if not ext.lower() in valid_extensions:
                raise ValidationError('Unsupported file extension.')
            else:
                file = Files.objects.create(post_id=post.id, file=request.FILES['file'])
                file.save()

    return render(request, 'account/create_post.html')


@login_required(login_url='/login/')
def User_post(request, user_id):
    posts = Post_user.objects.filter(user_id=user_id)
    likes = Post_like.objects.filter(user=user_id)
    print(likes)
    cate = Category_user.objects.all()
    images = Images.objects.all()
    videos = Videos.objects.all()
    voices = Voices.objects.all()
    files = Files.objects.all()
    context = {
        'user': request.user.user_id,
        'categories': cate,
        'posts': posts,
        'images': images,
        'videos': videos,
        'voices': voices,
        'files': files,
        'likes':likes

    }
    return render(request, 'account/posts.html', context)


@login_required(login_url='/login/')
def Post_details(request, post_id):
    context = {
        'post':  get_object_or_404(Post_user, id=post_id),
        'comments':  Post_comment.objects.filter(post_id_id=post_id),
    }
    return render(request, 'account/post_details.html', context)


class edit_post(UpdateView):
    model = Post_user
    template_name = 'account/update_post.html'
    fields = ['title', 'description']


def delete_post(request, post_id):
    Post_user.objects.filter(id=post_id).delete()
    return redirect('account:profile')


@login_required(login_url='/login/')
def Search_user(request, username):
    context = {
        'username': User.objects.get(username=username)
    }
    return render(request, 'account/search.html', context)


@login_required(login_url='/login/')
def User_Update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid() or user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Update Successfully', 'success')
            return redirect('account:profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'account/update.html', context)


@login_required(login_url='/login/')
def Change_Password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password is successfully changed')
            return redirect('account:profile')
        else:
            messages.error(request, 'Password is wrong!', 'danger')
            return redirect('account:change')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change.html', {'form': form})


@login_required(login_url='/login/')
def like(request):
    if request.method == "POST":
        post_id = request.POST["post_id"]
        user_like = Post_like.objects.filter(user=request.user.user_id)
        post_like = Post_like.objects.filter(post=post_id)

        if Post_like.objects.filter(user=request.user.user_id, post=post_id).exists():
            Post_like.objects.filter(user=request.user.user_id,post=post_id).delete()
            print("dissliked")
            return HttpResponse("dissliked")
        else:
            newLike = Post_like(user_id=request.user.user_id, post_id=post_id)
            newLike.save()
            print("liked")
            return HttpResponse("liked")


@login_required(login_url='/login/')
def follow(request):
    if request.method == "POST":
        user_id= request.POST['user_id']
        self_id = request.user.user_id
        if user_id and self_id:
            if User_Follow.objects.filter(user_id=user_id, self_id=self_id).exists():
                User_Follow.objects.filter(user_id=user_id, self_id=self_id).delete()
                print("unfollowed")
                return HttpResponse("unfollowed")
            else:
                newFollow = User_Follow(user_id=user_id, self_id=self_id)
                newFollow.save()
                print("followed")
                return HttpResponse("followed")
        else:
            return HttpResponse("error")


@login_required(login_url='/login/')
def block(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        self_id = request.user.user_id
        if user_id and self_id:
            if User_Block.objects.filter(user_id=user_id, self_id=self_id).exists():
                User_Block.objects.filter(user_id=user_id, self_id=self_id).delete()
                print("unblocked")
                return HttpResponse("unblocked")
            else:
                newBlock = User_Block(user_id=user_id, self_id=self_id)
                newBlock.save()
                print("blocked")
                return HttpResponse("blocked")
        else:
            return HttpResponse("error")


@login_required(login_url='/login/')
def comment(request):
    if request.method == "POST":
        post_comment = request.POST['post_id']
        post = get_object_or_404(Post_user,id = post_comment)
        description = request.POST['description']
        print("income")
        comment_id = None
        if request.user.user_id and post_comment:
            if comment_id:
                save_comment = Post_comment(user_id=request.user, comment_id=comment_id, post_id=post, description=description)
                save_comment.save()
                return HttpResponse("success")
            else:
                save_comment = Post_comment(user_id=request.user, comment_id=comment_id, post_id=post, description=description)
                save_comment.save()
                print("saved")
                return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")


@login_required(login_url='/login/')
def category(request, title):
    context = {
        'category': get_object_or_404(Category_user, title=title, status=True)
    }
    return render(request, "account/category.html", context)


def report(request):
    if request.method == "POST":
        user_id = request.user.user_id
        post_id = request.POST['post_id']
        if user_id and post_id:
            if Report.objects.filter(user_id=user_id,post_id=post_id).exists():
                return HttpResponse("error")
            else:
                reports = Report(user_id=user_id,post_id=post_id)
                reports.save()
                return HttpResponse("success")