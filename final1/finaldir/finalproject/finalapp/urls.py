from django.contrib import admin
from django.urls import path,include
from .import views
app_name='finalapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('new',views.new,name='new'),
    path('form',views.form,name='form'),
]
