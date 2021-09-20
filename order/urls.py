from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
                  path('', views.order_basket, name='order_basket'),
                  path('order-submit/', views.order_submit, name='order_submit'),
                  path('order-confirm/', views.order_confirm, name='order_confirm'),
                  path('order-history/', views.order_history, name='order_history'),
                  path('order-history-latest/', views.order_history_latest, name='order_history_latest'),

              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)  # is this import of setting correct? check this later
