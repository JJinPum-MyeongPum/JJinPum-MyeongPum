from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import auth


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        
        if user is not  None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
        
def logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST" :
        user = User.objects.create_user(
            username = request.POST["username"],
            password = request.POST["password"],
            nickname = request.POST["nickname"],
            profileImg = request.FILES["profileImg"]
        )
        user.save()
        auth.login(request, user)
        return redirect('home')
    else : 
        return render(request,'signup.html')
# Create your views here.
