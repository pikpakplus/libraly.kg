from django.http import HttpResponse
from datetime import datetime
from . import models
from django.shortcuts import render, get_object_or_404  # Added get_object_or_404 for book_detail_view


def book_list_view(request):
    if request.method == 'GET':
        query = models.BooksModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html',
                      context=context_object_name)


def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BooksModel, id=id)
        context_object_name = {
            'book_id': query
        }
        return render(request, template_name='book_detail.html',
                      context=context_object_name)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse(
            'Здравствуйте! Добро пожаловать на мой веб-сайт.)')


def photo(request):
    if request.method == 'GET':
        return HttpResponse(
            "<img src='https://avatars.mds.yandex.net/i?id=3351486e8810cb55045d6d7749e98828_l-5869106-images-thumbs&n=13.jpg' />")


def time(request):
    if request.method == 'GET':
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"<h1>Текущее время:</h1><p>{now}</p>")