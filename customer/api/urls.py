from django.urls import path

from customer.api.views import CreateCustomer, CreateUser

urlpatterns = [
    path('create-customer/', CreateCustomer.as_view(), name='create_customer'),
    path('create-user/', CreateUser.as_view(), name='create_user'),

]
