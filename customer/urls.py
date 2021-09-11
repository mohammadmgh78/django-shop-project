from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'customer'
urlpatterns = [
                  path('create-customer/', views.create_cutomer, name='create_customer'),
                  path('', views.home, name='home'),

              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)  # is this import of setting correct? check this later
