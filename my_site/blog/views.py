from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return HttpResponse("Главная страница")


def posts(request):
    return HttpResponse("Все посты блога")

def get_post_by_number(request, number_post):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")


def get_post(request, name_post):
    return HttpResponse(f"Здесь содержится информация о посте {name_post}")
