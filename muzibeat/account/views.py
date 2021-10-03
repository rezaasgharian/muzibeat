from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import administrator
from django.urls import reverse
from shortuuidfield import ShortUUIDField
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse(administrator.views.Posts))
        else:
            context = {
                "username": username,
                "errormessage": "User not found"
            }
            return render(request, "account/login.html", context)
    else:
        return render(request, 'account/login.html',{})


def Register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username= data['username'], email= data['email'] , password= data['password'])
            return redirect('login')
    else:
        form = UserCreateForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)



def Logout_view(request):
    logout(request)
    return redirect('login')

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
# >>>>>>> c1bef300c8a185fd8c7cbf9ca31d620a64f54636
