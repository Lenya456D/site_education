# Generated by Django 4.2.1 on 2024-04-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationsLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Заголовок')),
                ('link', models.CharField(db_index=True, max_length=255, verbose_name='Ссылка')),
            ],
        ),
    ]
