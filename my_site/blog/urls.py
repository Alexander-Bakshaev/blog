from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('blog/', views.posts),
    path('posts/', views.posts),
    path('posts/<int:number_post>', views.get_post_by_number),
    path('posts/<str:name_post>', views.get_post),
]
