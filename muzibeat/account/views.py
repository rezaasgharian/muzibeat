from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
import administrator
from django.urls import reverse
from .forms import UserRegisterForm

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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username= data['user_name'], email= data['email'], first_name= data['first_name'], last_name= data['last_name'], password= data['password_1'])
            return redirect('administrator:login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'account/register.html', context)

def Logout_View(request):
    logout(request)
    return redirect('login')
