from django.urls import path
from .views import register,loginpage,home,logoutuser



urlpatterns = [
    path('',register, name='register'),
    path('login/',loginpage,name='login'),
    path('home/',home,name='home'),
    path('logoutuser/',logoutuser,name='logoutuser')
]
