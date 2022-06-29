from django.forms import ModelForm, TextInput
from .models import Tournament, Match, Event
from commands.models import Command
from django import forms


class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = ['title', 'info', 'start_date', 'background']


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ['date_and_time', 'tournament', 'command_a', 'command_b']