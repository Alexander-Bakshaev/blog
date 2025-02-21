from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def main_page(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return render(request, 'blog/list_detail.html')

def get_post_by_number(request, number_post):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")


def get_post(request, name_post):
    return HttpResponse(f"Здесь содержится информация о посте {name_post}")
