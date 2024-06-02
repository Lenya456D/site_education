from django.db import models


# Create your models here.

class EducationsLinks(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    link = models.CharField(max_length=255, db_index=True, verbose_name='Ссылка')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
