from django.urls import path, include

urlpatterns = [
    path('users-api/', include('users.api.urls')),
    path('cutomer-api/', include('customer.api.urls')),
]
