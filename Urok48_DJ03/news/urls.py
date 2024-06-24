from django.urls import path
from . import views

urlpatterns = [
    # Здесь указывается относительный путь онтосительно пути
    # на котором сработал инклуд родительского urls.py
    path('', views.func_home, name='news_home')
]