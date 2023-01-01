# Generated by Django 4.1.4 on 2023-01-01 20:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0003_alter_quizelement_memorycard'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteUserCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ManyToManyField(to='words.memorycard', verbose_name='Karta')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
            options={
                'verbose_name': 'Ulubiona karta',
                'verbose_name_plural': 'Ulubione karty',
            },
        ),
    ]
