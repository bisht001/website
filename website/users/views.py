from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def signup(request):
    return render(request,'users/signup.html')

# Create your views here.
def signup_func(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup_page')


        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('signup_page')

        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()

            user_login = auth.authenticate(username=username,password=password)
            auth.login(request,user_login)
            return redirect('#')

    return render(request,'signup_page')


def login(request):
    return render(request,'users/login.html')

def login_func(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_login = auth.authenticate(username=username, password=password)
        if user_login is None:
            messages.info(request,'Incorrect data')
            return redirect('signup_page')

        auth.login(request, user_login)
        return redirect('#')

    else:
        return render(request,'users/login.html')

@login_required(login_url='login_page')
def logout(request):
    auth.logout(request)
    return redirect('login_page')
