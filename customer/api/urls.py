from django.urls import path

from customer.api.views import CreateCustomerAPI, ChangePasswordView

urlpatterns = [
    path('create-customer-api/', CreateCustomerAPI.as_view(), name='create_customer_api'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

]
