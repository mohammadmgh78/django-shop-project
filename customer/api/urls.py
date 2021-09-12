from django.urls import path, include

from customer.api.views import CreateCustomerAPI, ChangePasswordView

urlpatterns = [
    path('create-customer-api/', CreateCustomerAPI.as_view(), name='create_customer_api'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]
