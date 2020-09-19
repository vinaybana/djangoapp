from django.contrib import admin	
from django.urls import path
from .import views


app_name = 'blog'

urlpatterns = [
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/new/', views.post_new, name='post_new'),
	path('blog/sign_up/',views.sign_up,name="sign-up"),
	path('blog/logout/',views.logout, name="logout"),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('login/',views.login, name="login"),
    path('', views.post_list, name ='post_list'),
    path('userdetail/<int:pk>/',views.userdetail, name='userdetail'),
    path('edituser/<int:pk>/', views.edit_profile, name='edit_profile'),


    
    
    ]