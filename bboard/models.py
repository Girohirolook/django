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
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']


class Rubric(models.Model):
    rubric = models.CharField(max_length=50, verbose_name='Рубрика')

    def __str__(self):
        return self.rubric
