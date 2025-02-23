from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    
]
