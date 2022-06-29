from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Command(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='commands/logo/', blank=True, verbose_name="Логотип")
    command_photo = models.ImageField(upload_to='commands/photo/', blank=True, verbose_name="командное фото")

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="player")
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамиля', max_length=50)
    date_of_birth = models.DateField(verbose_name='Дата рождения',)

    photo = models.ImageField(upload_to='player/', blank=True, verbose_name="Фото")

    # blank = True
    # default = 'static/img/player.jpg'

    KEEPER = "Вратарь"
    DEFENDER = "Защитник"
    MIDFIELDER = "Полузащитник"
    FORWARD = "Нападающий"

    ROLES = [
        (KEEPER, "Вратарь"),
        (DEFENDER, "Защитник"),
        (MIDFIELDER, "Полузащитник"),
        (FORWARD, "Нападающий"),
    ]

    role = models.CharField(verbose_name='Амплуа', max_length=50, choices=ROLES)
    is_captain = models.BooleanField(verbose_name="Капитан", default=False)
    command = models.ForeignKey(Command, on_delete=models.CASCADE, verbose_name='Команда', related_name='players')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
