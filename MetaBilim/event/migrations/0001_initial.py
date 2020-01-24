# Generated by Django 2.2.5 on 2020-01-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('summary', models.TextField(verbose_name='Краткое описание')),
                ('event_type', models.IntegerField(choices=[(1, 'Гранты'), (6, 'Конференции'), (5, 'Курсы'), (3, 'Стипендии'), (2, 'Стажировки'), (4, 'Конкурсы')], verbose_name='Тип')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('deadline', models.DateTimeField(blank=True, verbose_name='Дэдлайн')),
                ('detailed_information', models.TextField(verbose_name='Подробное описание')),
                ('thumb', models.ImageField(upload_to='', verbose_name='Image')),
                ('background', models.ImageField(upload_to='', verbose_name='Background')),
                ('link', models.CharField(max_length=4096, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=70, verbose_name='Город')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='event.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='events', to='event.Tag'),
        ),
    ]