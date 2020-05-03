
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('cutomerlogin/',views.Customerlogin, name='Customerlogin'),
    path('stafflogin/',views.Stafflogin, name='Stafflogin'),
    path('logout/', views.handleLogout, name='logout'),
    path('reception/',views.Handlereception, name='Handlereception'),
    path('cutomer/',views.Handlecustomer, name='Handlecustomer'),
]