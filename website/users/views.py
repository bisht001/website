from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def signup(request):
    return render(request,'users/signup.html')

def signup_func(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already taken')
            return redirect('signup_page')

        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already registered')
            return redirect('signup_page')

        else:
            try:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                messages.success(request, 'Account created successfully!')
                return redirect('home_page')
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
                return redirect('signup_page')

    return render(request,'signup_page')

def login(request):
    return render(request,'users/login.html')

def login_func(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_login = auth.authenticate(username=username, password=password)
        if user_login is None:
            messages.error(request,'Invalid credentials')
            return redirect('login_page')

        auth.login(request, user_login)
        messages.success(request, 'Logged in successfully!')
        return redirect('home_page')

    return render(request,'users/login.html')

@login_required(login_url='login_page')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login_page')