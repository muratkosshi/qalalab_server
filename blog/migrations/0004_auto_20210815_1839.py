# Generated by Django 3.2.6 on 2021-08-15 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210814_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider1',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slider1', to='blog.projects', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='slider2',
            name='news',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slider2', to='blog.news', verbose_name='Новость'),
        ),
        migrations.AlterField(
            model_name='slider3',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slider3', to='blog.event', verbose_name='Мероприятие'),
        ),
    ]
