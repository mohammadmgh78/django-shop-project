from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'product'
urlpatterns = [
                  path('add-product/', views.add_product, name='add_product'),

              ]