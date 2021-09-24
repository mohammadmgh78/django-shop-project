from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils.datetime_safe import date

from customer.models import Customer, Discount
from order.models import Order, OrderHistory


def order_basket(request):
    customer = Customer.objects.filter(owner=request.user).first()
    try:
        order = Order.objects.filter(user=customer).first()
        # print(order.order_status)
        # if order.order_status == 'Not Selected':
        #     pass
        # else:
        #     order= None
    except AttributeError:
        order = None
    print(customer)
    print(order)
    return render(request, 'order/order_basket.html', {'order': order})


def order_submit(request):
    my_dict = dict(request.POST)
    prices = [float(price) for price in my_dict['product_price']]
    numbers = [int(number) for number in my_dict['number_of_products']]
    total_price = []
    print(prices)
    print(numbers)
    print(prices[0] * numbers[0])
    for price, number in zip(prices, numbers):
        total_price.append(price * number)
    customer = Customer.objects.filter(owner=request.user).first()
    try:
        discount = Discount.objects.filter(customer=customer)
        discount = int(discount.discount_amount)
    except AttributeError:
        discount = 0

    print(discount)
    total_price_all = sum(total_price)
    return render(request, 'order/order_submit.html', {'total_price_all': total_price_all, 'discount': discount})


def order_confirm(request):
    customer = Customer.objects.filter(owner=request.user).first()
    order = Order.objects.filter(user=customer).first()
    order.order_status = 'confirmed'
    order.save()
    order_history = OrderHistory(order=order, user=customer)
    order_history.save()
    return redirect('http://127.0.0.1:8000/customer/')


def order_history(request):
    customer = Customer.objects.filter(owner=request.user).first()
    customer_order_history = OrderHistory.objects.filter(user=customer)
    return render(request, 'order/order_history.html', {'customer_order_history': customer_order_history})


def order_history_latest(request):
    customer = Customer.objects.filter(owner=request.user).first()
    enddate = date.today()
    startdate = enddate - timedelta(days=6)
    orders = Order.objects.filter(date_submitted__range=[startdate, enddate], user=customer)
    print(orders)
    return render(request, 'order/order_history_latest.html', {'orders': orders})
