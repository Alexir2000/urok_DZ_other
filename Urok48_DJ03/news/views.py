from django.shortcuts import render
from .models import News_post

# Create your views here.



def func_home(request):
    news_all = News_post.objects.all()

    # Можно брать файл из темплейта другого приложения.
    # так можно делать. Можно обращаться к файлам параллельного приложения.
    return render(request, 'news/news.html', {'news': news_all})
