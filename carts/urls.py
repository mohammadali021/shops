from django.urls import path

from carts import views

urlpatterns = [
    path('' , views.ViewCarts , name='carts'),
    path('add-cart/', views.CartAdd, name='add_carts'),

]