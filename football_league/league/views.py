from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Players


def home(request):
    return render(request, 'league/home.html')


def get_players(request):
    player = Players.objects.all()
    return render(request, 'league/players.html', {'player': player})
