from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
              path('blogpost/<int:post_id>', views.blogpost,name="blogPost"),
              path('', views.index, name="blog"),
              path('', views.index, name="blog"),
              path('', views.index, name="blog"),
              path('', views.index, name="blog"),
              path('', views.index, name="blog"),
]