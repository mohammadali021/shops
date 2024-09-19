from django.urls import path

from shops import views


urlpatterns = [
    path('<slug:s>', views.product_details, name='product_details'),
    path('category/<slug:s>' , views.product_category , name='product_category'),
    path('', views.Viewmain, name='main'),
    path('about/', views.AboutUs, name='about'),
    path('login/', views.Login_User, name='login'),
    path('logout/', views.Logout_User, name='logout'),
    path('sign-in/', views.sign_info, name='sign-in'),
    path('category/',views.category , name='category'),


]
