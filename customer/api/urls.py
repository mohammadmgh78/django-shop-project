from django.urls import path

from customer.api.views import  CreateCustomerAPI

urlpatterns = [
    path('create-customer-api/', CreateCustomerAPI.as_view(), name='create_customer_api'),

]
