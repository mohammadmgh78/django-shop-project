from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()


def login_user(request):
    print('hello')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/university/')

    return render(request, 'users/base.html')

# def logout_user(request):
#     logout(request)
#     print('success')
#     return render(request, 'users/login.html')
