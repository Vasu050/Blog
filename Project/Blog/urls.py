from django.contrib import admin
from django.urls import path
from Blog import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('delete/<int:id>/', views.delete_blog, name='delete_blog'),
    path('update/<int:id>/', views.update_blog, name='update_blog'),
    path('add',views.add_blog,name='add_blog'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail')
]
