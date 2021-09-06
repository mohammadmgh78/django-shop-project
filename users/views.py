from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()


def login_user(request):
    print('1')
    if request.method == 'POST':
        print('2')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/')

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')


def register_user(request):
    pass