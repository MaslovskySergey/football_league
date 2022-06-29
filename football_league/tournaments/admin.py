from django.contrib import admin
from .models import Tournament, Match, Event
from commands.models import Command, Player


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'info',
        'start_date',
        "get_commands",
        "background",
    ]

    @admin.display(description="Commands")
    def get_commands(self, tur: Tournament):
        return list(tur.commands.all())


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        'tournament',
        'date_and_time',
        'command_a',
        'command_b',
    ]

    # @admin.display(description="Command_a")
    # def get_command_a(self, obj: Command):
    #     return obj.
    #
    # @admin.display(description="Commands")
    # def get_command_b(self, com: Command):
    #     return list(com.command_b)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'minute',
        'scored',
        'assistant',
        'get_a_card',
        'event',
        'color_card',
    ]

    list_editable = [
        'event',
        'color_card',
    ]

    @admin.display(description="Players")
    def get_players(self, com: Player):
        return list(com.players.all())