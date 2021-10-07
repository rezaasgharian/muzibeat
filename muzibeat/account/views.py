from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import administrator
from django.urls import reverse
from shortuuidfield import ShortUUIDField
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.
@login_required(login_url='/login/')
def Profiles(request):
    context={
        'profile': Profile.objects.get(user_id=request.user.user_id)
    }
    return render(request,'account/profile.html',context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("account:profile")
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "account/login.html", context)
    else:
        if request.user.is_authenticated:
            return redirect('account:profile')
        return render(request, 'account/login.html',{})

def Register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username= data['username'], email= data['email'] , password= data['password'])
            user.save()
            return redirect('account:login')
    else:
        if request.user.is_authenticated:
            return redirect('account:profile')
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required(login_url='/login/')
def Logout_view(request):
    logout(request)
    return redirect('account:login')


def User_Update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Update Successfully','success')
            return redirect('account:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form':user_form, 'profile_form':profile_form}
    return render(request,'account/update.html', context)


def Change_Password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
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
    return render(request, 'account/change.html', {'form':form})






# def Email(request):
#     if form.is_valid():
#         subject = form.cleaned_data['subject']
#         message = form.cleaned_data['message']
#         sender = form.cleaned_data['sender']
#         cc_myself = form.cleaned_data['cc_myself']
#
#         recipients = ['info@example.com']
#         if cc_myself:
#             recipients.append(sender)
#
#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect('/thanks/')
