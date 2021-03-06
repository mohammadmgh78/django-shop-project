from django.http import HttpResponse
from django.shortcuts import render, redirect

from customer.models import Customer, Manager, Staff
from product.models import Product, Category


def create_cutomer(request):
    if request.method == 'GET':
        print('create_customer in customer/views')
        return render(request, 'customer/register.html')
    if request.method == 'POST':
        print('create_customer in customer/views')
        return HttpResponse('hello')


def home(request):
    logged_in = ''
    try:
        if Manager.objects.filter(owner=request.user):
            logged_in = 'manager'
        elif Staff.objects.filter(owner=request.user):
            logged_in = 'staff'
        elif Customer.objects.filter(owner=request.user):
            logged_in = 'customer'
    except:
        logged_in = ''

    try:
        if request.GET['select_category'] == 'none':
            products = Product.objects.all()
        else:
            category = Category.objects.filter(pk=request.GET['select_category']).first()
            products = category.product_set.all()
    except:
        products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'customer/home.html',
                  {'logged_in': logged_in, 'products': products, 'categories': categories})


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


def profile_customer(request):
    if request.method == "GET":
        customer = Customer.objects.filter(owner=request.user).first()
        return render(request, 'customer/profile.html', {'customer': customer})
    if request.method == "POST":
        customer = Customer.objects.filter(owner=request.user).first()
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.city_born = request.POST['city_born']
        customer.closest_friend = request.POST['closest_friend']
        customer.username = request.POST['username']
        customer.save()
        return render(request, 'customer/profile.html', {'customer': customer})


def customer_change_password(request):
    return render(request, 'customer/change_password.html')


def customer_forgot_password(request):
    return render(request, 'customer/forgot_password.html')


def customer_reset_password(request):
    return render(request, 'customer/reset_password.html')


def create_staff(request):
    if request.method == 'GET':
        print('create_staff in customer/views')
        return render(request, 'customer/register_staff.html')
