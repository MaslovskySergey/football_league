from django.contrib import admin
from .models import Command, Player


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'logo',
        'command_photo',
        "get_players",
    ]

    @admin.display(description="Players")
    def get_players(self, com: Command):
        return list(com.players.all())


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'date_of_birth',
        'role',
        'command',
        'get_goals',
        'photo',
    ]

    list_editable = [
        'role',

    ]

    @admin.display(description="goals")
    def get_goals(self, obj: Player):
        return obj.goals.count()