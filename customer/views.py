from django.http import HttpResponse
from django.shortcuts import render, redirect


def create_cutomer(request):
    if request.method == 'GET':
        print('create_customer in customer/views')
        return render(request, 'customer/register.html')
    if request.method == 'POST':
        print('create_customer in customer/views')
        return HttpResponse('hello')


def home(request):
    return render(request, 'customer/home.html')


from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


# Create your views here.


def login_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/customer/')

    return render(request, 'customer/login.html')


def logout_customer(request):
    logout(request)
    print('success')
    return render(request, 'customer/login.html')
