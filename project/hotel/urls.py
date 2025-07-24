from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeHotel, name="homeHotel"),
    path('loginCustomer', views.loginCustomer, name="loginCustomer"),
    path('logoutCustomer', views.logoutCustomer, name="logoutCustomer"),
    path('signupCustomer', views.signupCustomer),
    path('customerHome', views.customerHome, name="customerHome"),

    
]
