from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def main_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_post_by_number(request, number_post):
    response = {
        'number_post': number_post,
    }
    return render(request, 'blog/detail_by_number.html', context=response)


def get_post(request, name_post):
    response = {
        'name_post': name_post,
    }
    return render(request, 'blog/detail_by_name.html', context=response)