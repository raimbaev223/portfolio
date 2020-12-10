from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    img = models.ImageField(null=True, blank=True, upload_to='portfolio/static/images/portfolio', verbose_name='Изображение')
    description = models.TextField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.title


