from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from time import time

User = get_user_model()

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Event(models.Model):
    title = models.CharField(verbose_name='Заголовок', db_index=True, max_length=150)
    summary = models.TextField(verbose_name='Краткое описание')
    TYPES = {
        (1, "Гранты"),
        (2, "Стажировки"),
        (3, "Стипендии"),
        (4, "Конкурсы"),
        (5, "Курсы"),
        (6, "Конференции"),
    }
    event_type = models.IntegerField(verbose_name='Тип', choices=TYPES)
    date = models.DateTimeField(verbose_name='Дата')
    deadline = models.DateTimeField(verbose_name='Дэдлайн', blank=True)
    #location
    detailed_information = models.TextField(verbose_name='Подробное описание')
    thumb = models.ImageField(verbose_name='Image') #Пока не знаю как в REST показывать имг
    background = models.ImageField(verbose_name='Background')
    tags = models.ManyToManyField('Tag', blank=True, related_name='events')
    link = models.CharField(verbose_name='Ссылка', max_length=4096)

class Location(models.Model):
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=70)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    event = models.ForeignKey(Event, related_name='location', on_delete=models.CASCADE)


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True, unique=True)
