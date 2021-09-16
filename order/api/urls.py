from django.urls import path

from order.api.views import create_order_api

urlpatterns = [
    path('create-order-api/<int:ids>', create_order_api, name='create_order_api'),


]