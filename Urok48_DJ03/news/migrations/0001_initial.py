# Generated by Django 5.1a1 on 2024-06-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название нновости')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание новости')),
                ('text', models.TextField(verbose_name='Новость')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
            ],
        ),
    ]
