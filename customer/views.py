from django.http import HttpResponse
from django.shortcuts import render

def create_cutomer(request):
    if request.method == 'GET':
        print('create_customer in customer/views')
        return render(request, 'customer/register.html')
    if request.method == 'POST':
        print('create_customer in customer/views')
        return HttpResponse('hello')

def home(request):
    return render(request, 'customer/home.html')