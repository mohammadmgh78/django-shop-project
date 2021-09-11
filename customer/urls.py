from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
                  path('create-customer/', views.create_cutomer, name='create_customer'),
                  path('', views.home, name='home'),
                  path('login-customer/', views.login_customer, name='login_customer'),
                  path('logout-customer/', views.logout_customer, name='logout_customer'),
                path('profile-customer/', views.profile_customer, name='profile_customer'),

              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)  # is this import of setting correct? check this later
