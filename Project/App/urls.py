from django.contrib import admin
from django.urls import path
from App import views
urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('register',views.register,name='register'),
    # path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
