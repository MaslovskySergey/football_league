from django.urls import path
from . import views


urlpatterns = [
    path('', views.TournamentsView.as_view(), name='tournaments'),
    path('info/<int:tournament_id>', views.InfoTournamentView.as_view(), name='id_tournament'),
    path('about/<int:id>/', views.AboutTournamentView.as_view(), name='about'),
    path('commands/<int:tournament_id>/', views.CommandsTournamentView.as_view(), name='commands_tournament'),
    path('matches/<int:tournament_id>/', views.MatchesTournamentView.as_view(), name='matches_tournament'),
    path('match/<int:match_id>', views.MatchView.as_view(), name='match'),

    path('table/<int:tournament_id>/<type>/', views.TournamentTableView.as_view(), name="tournament_table")



]
