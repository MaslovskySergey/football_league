from django.db import models

# Create your models here.


class Players(models.Model):
    name = models.CharField('Фамилия имя', max_length=50)
    age = models.IntegerField('Возраст', default=0)
    goals = models.IntegerField('Голы', default=0)
    cards = models.IntegerField('Карточки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'