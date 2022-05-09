from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True)
    KINDS = (
        ('Куплю', 'Куплю'),
        ('Продам', 'Продам'),
        ('Обменяю', 'Обменяю'),
    )
    kind = models.CharField(max_length=50, choices=KINDS, blank=True, verbose_name='Тип')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']