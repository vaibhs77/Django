from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
              path('', views.index, name="Shopname"),
              path('about/', views.about, name="aboutus"),
              path('contact/', views.contact, name="contactus"),
              #path("products/<int:myid>", views.productview, name="ProductView"),
              path("products/<int:myid>", views.productView, name="ProductView"),
              path('checkout/', views.checkout, name="checkout"),
              path('tracker/', views.tracker, name="tracker"),
              path('search/', views.search, name="search"),
             ]

 #path("products/<int:myid>", views.productView, name=),