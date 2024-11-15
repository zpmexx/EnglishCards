# Generated by Django 4.1.4 on 2022-12-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemoryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polishName', models.CharField(default='defaultpolishword', max_length=50, verbose_name='Polskie słowo')),
                ('englishName', models.CharField(default='defaultenglishword', max_length=50, verbose_name='Angielskie słowo')),
                ('polishDescription', models.CharField(default='defaultpolishdescription', max_length=500, verbose_name='Polski opis')),
                ('englishDescription', models.CharField(default='defaultenglishdescription', max_length=500, verbose_name='Angielski opis')),
                ('wordLevel', models.IntegerField(choices=[(0, 'A1'), (1, 'A2'), (2, 'B1'), (3, 'B2'), (4, 'C1'), (5, 'C2')], default=0, verbose_name='Poziom słówka')),
                ('confirmation_status', models.IntegerField(choices=[(0, 'zatwierdzone'), (1, 'niezatwierdzone')], default=0, verbose_name='Status')),
            ],
        ),
    ]
