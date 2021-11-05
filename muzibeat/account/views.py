from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.views.generic.edit import UpdateView
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
    context = {
        'profile': Profile.objects.get(user_id=request.user.user_id),
        # 'post' : Post_user.objects.filter(user_id=user_id),
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

        if request.FILES.get('thumbnail', False):
            image = request.FILES['thumbnail']
            ext = os.path.splitext(str(image))[1]
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if not ext.lower() in valid_extensions:
                raise ValidationError('Unsupported file extension`.')
            else:
                img = Images.objects.create(post_id=post.id, thumbnail=request.FILES['thumbnail'])
                img.save()

        if request.FILES.get('video', False):
            vid = request.FILES['video']
            ext = os.path.splitext(str(vid))[1]
            valid_extensions = ['.mp4', '.mkv', '.mov', '.wmv']
            if not ext.lower() in valid_extensions:
                raise ValidationError('Unsupported file extension.')
            else:
                video = Videos.objects.create(post_id=post.id, file=request.FILES['video'])
                video.save()

        if request.FILES.get('voice', False):
            voc = request.FILES['voice']
            ext = os.path.splitext(str(voc))[1]
            valid_extensions = ['.mp3', '.ogg', '.aac']
            if not ext.lower() in valid_extensions:
                raise ValidationError('Unsupported file extension.')
            else:
                voice = Voices.objects.create(post_id=post.id, file=request.FILES['voice'])
                voice.save()

        if request.FILES.get('file', False):
            fil = request.FILES['file']
            ext = os.path.splitext(str(fil))[1]
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
    images = Images.objects.all()
    videos = Videos.objects.all()
    voices = Voices.objects.all()
    files = Files.objects.all()
    context = {
        'user': request.user.user_id,
        'posts': posts,
        'images': images,
        'videos': videos,
        'voices': voices,
        'files': files

    }
    return render(request, 'account/posts.html', context)


class edit_post(UpdateView):
    model = Post_user
    template_name = 'account/update_post.html'
    fields = ['title','description']


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
