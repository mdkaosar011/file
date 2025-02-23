from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('my_post/', views.my_post, name='my_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path("profile/",views.profile_view, name='profile' ),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),



]