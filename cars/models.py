from django.db import models
from django.db.models import CASCADE


class Brand(models.Model):
    """Модель марки автомобиля с полем название марки"""
    name = models.TextField(verbose_name='Название марки')


class Model(models.Model):
    """Модель модели автомобиля с полем название модели
    и внешним ключом на марку автомобиля"""
    brand = models.ForeignKey(Brand, related_name='Марка', on_delete=CASCADE)
    name = models.TextField(verbose_name='Название модели')
