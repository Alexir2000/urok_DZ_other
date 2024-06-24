from django.db import models

# Create your models here.

class News_post(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Название нновости')
    short_description = models.CharField(verbose_name='Краткое описание новости', max_length=200)
    text = models.TextField(verbose_name='Новость')
    pub_date = models.DateTimeField(verbose_name='дата публикации')
    user_name = models.TextField(max_length=100, verbose_name='Автор')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
