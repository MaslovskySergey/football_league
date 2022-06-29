from django.db import models
from commands.models import Command, Player


class Tournament(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField(blank=True, null=True, verbose_name="Информация о турнире")
    start_date = models.DateField(verbose_name='Дата начала турнира',)
    commands = models.ManyToManyField(Command, related_name='tournaments')
    background = models.ImageField(upload_to='tournament', blank=True, verbose_name="Фон турнира")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} {self.start_date}"


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True, related_name='matches')
    date_and_time = models.DateTimeField()
    command_a = models.ForeignKey(Command, on_delete=models.CASCADE, null=True, related_name='+')
    command_b = models.ForeignKey(Command, on_delete=models.CASCADE, null=True, related_name='+')
    status = models.BooleanField(verbose_name="Статус", default=False)

    class Meta:
        ordering = ['-date_and_time']

    def __str__(self):
        return f"{self.command_a} {self.date_and_time} {self.command_b}"


class Event(models.Model):
    match = models.ForeignKey(Match, related_name='events', on_delete=models.CASCADE)
    minute = models.IntegerField()
    # command = models.ManyToManyField(Command)

    GOAL = "Гол"
    CARD = "Карточка"

    EVENT = [
        (GOAL, "Гол"),
        (CARD, "Карточка"),
    ]

    event = models.CharField(verbose_name='Событие', max_length=50, choices=EVENT)
    scored = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, related_name="goals")
    assistant = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, related_name="assists")

    RED = "Красная"
    YELLOW = "Желтая"

    COLORS = [
        (RED, "Красная"),
        (YELLOW, "Желтая"),
    ]

    color_card = models.CharField(verbose_name='Карточка', max_length=50, choices=COLORS, blank=True)
    get_a_card = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, related_name='cards', null=True)


