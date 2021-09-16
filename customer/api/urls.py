from django.urls import path, include

from customer.api.views import CreateCustomerAPI, ChangePasswordView, CreateStaffAPI

urlpatterns = [
    path('create-customer-api/', CreateCustomerAPI.as_view(), name='create_customer_api'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('create-staff-api/', CreateStaffAPI.as_view(), name='create_staff_api'),

]
