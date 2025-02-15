from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.main_page),
    path('blog/', views.blog),
]
