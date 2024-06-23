from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(
        """
        <h1>Привет! Это домашняя страница сайта!</h1>
        <ul> <li><a href="/new">Перейти на страницу NEW</a></li>
            <li><a href="/data">Перейти на страницу DATA</a></li>
            <li><a href="/test">Перейти на страницу TEST</a></li> </ul>
    """)
def func_new(request):
    return HttpResponse("""
        <h1>Привет! Это ВТОРАЯ страница сайта!</h1>
        <p><a href="/">Вернуться на главную страницу</a></p>
    """)
def func_data(request):
    return HttpResponse("""
        <h1>Привет! Это страница DATA !</h1>
        <p>Вот некоторые интересные данные.</p>
        <p><a href="/">Вернуться на главную страницу</a></p>
    """)
def func_test(request):
    return HttpResponse("""
        <h1>Привет! Это страница TEST!</h1>
        <p>Здесь можно провести тесты.</p>
        <p><a href="/">Вернуться на главную страницу</a></p>
    """)