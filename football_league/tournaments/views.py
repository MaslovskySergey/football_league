from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
# from .forms import CommandForm, PlayerForm
from .models import Tournament, Match, Event
from .forms import TournamentForm, MatchForm
from commands.models import Command


class TournamentsView(View):
    def get(self, request, *args, **kwargs):
        tournaments = Tournament.objects.all()

        data = {'tournaments': tournaments}

        if request.user.is_superuser:
            # data["form"] = TournamentForm(initial={"tournaments": tournaments})
            data["form"] = TournamentForm()
        return render(request, 'templates/tournaments/tournaments.html', context=data)

    def post(self, request, *args, **kwargs):
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            tournament = form.save()
            return redirect('id_tournament', tournament.pk)


class InfoTournamentView(View):
    def get(self, request, tournament_id, *args, **kwargs):
        tournament = get_object_or_404(Tournament, id=tournament_id)
        return render(request, 'templates/tournaments/info_tournament.html', context={
            "tournament": tournament
        })


class AboutTournamentView(View):
    def get(self, request, tournament_id, *args, **kwargs):

        tournament = get_object_or_404(Tournament, id=tournament_id)

        return render(request, 'templates/tournaments/about_tournament.html', context={
            "tournament": tournament
        })


class CommandsTournamentView(View):
    def get(self, request, tournament_id, *args, **kwargs):
        tournament = get_object_or_404(Tournament, id=tournament_id)
        commands_add = {}
        if request.user.is_superuser:
            commands_for_tournament = Command.objects.all()
            commands_add = []
            for commands in commands_for_tournament:
                if commands not in tournament.commands.all():
                    commands_add.append(commands)

        return render(request, "templates/tournaments/commands_tournament.html", context={
            "tournament": tournament,
            "commands_add": commands_add,
        })

    def post(self, request, tournament_id, *args, **kwargs):
        tournament = get_object_or_404(Tournament, id=tournament_id)
        form = request.POST
        if form.is_valid:
            for command in form:
                if command != "csrfmiddlewaretoken":
                    commands_add = form.get(command)
                    tournament.commands.add(commands_add)
        return redirect('commands_tournament', tournament.pk)

#
# class MatchesTournamentView(View):
#     def get(self, request, tournament_id, *args, **kwargs):
#         tournament = get_object_or_404(Tournament, id=tournament_id)

#         commands_in_tournament = tournament.commands.all()
#         #
#         # data = {"tournament": tournament,
#         #         "commands_in_tournament": commands_in_tournament}
#         data = {"tournament": tournament}
#
#         if request.user.is_superuser:
#             data["form"] = MatchForm()
#             data["commands_in_tournament"] = commands_in_tournament
#         return render(request, "templates/tournaments/matches_tournament.html", context=data)


class MatchesTournamentView(View):
    def get(self, request, tournament_id, *args, **kwargs):
        tournament = get_object_or_404(Tournament, id=tournament_id)



    def post(self, request, tournament_id, *args, **kwargs):
        tournament = get_object_or_404(Tournament, id=tournament_id)

        return redirect('matches_tournament', tournament.pk)


class MatchView(View):
    def get(self, request, match_id, *args, **kwargs):
        match = get_object_or_404(Match, id=match_id)
        return render(request, "templates/tournaments/match.html", context={
            'match': match
        })


class TournamentTableView(View):
    def get(self, request, tournament_id, type, *args, **kwargs):

        tournament_table = dict(
            # "command": {
            #     "self_command": command,
            #     "total_games": None,
            #     "wins": None,
            #     "draws": None,
            #     "losses": None,
            #     "goals_for": None,
            #     "goals_against": None,
            #     "points": None,
            # },
        )

        scorers_table = dict(
            # "last_name": {
            #     "self_player": player,
            #     "goals": None,
            # },
        )

        assistants_table = dict(
            # "last_name": {
            #     "self_player": player,
            #     "assist": None,
            # },
        )

        tournament = get_object_or_404(Tournament, pk=tournament_id)

        for command in tournament.commands.all():

            results = {
                "self_command": command,
                "total_games": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "goals_for": 0,
                "goals_against": 0,
                "points": 0,
            }

            played_matches = tournament.matches.filter(Q(command_a=command) | Q(command_b=command)).filter(status=True)

            for p_match in played_matches:
                all_events = p_match.events.filter(event=Event.GOAL)

                self_goals, other_goals = 0, 0

                for m_event in all_events:
                    if m_event.scored in command.players.all():
                        self_goals += 1
                    else:
                        other_goals += 1

                results["total_games"] = results.get("total_games", 0) + 1

                results["goals_for"] = results.get("goals_for", 0) + self_goals
                results["goals_against"] = results.get("goals_against", 0) + other_goals

                if self_goals > other_goals:
                    results["wins"] = results.get("wins", 0) + 1
                    results["points"] = results.get("points", 0) + 3
                elif self_goals < other_goals:
                    results["losses"] = results.get("losses", 0) + 1
                else:
                    results["draws"] = results.get("draws", 0) + 1
                    results["points"] = results.get("points", 0) + 1

            for player in command.players.all():
                scored_goal = {
                    "self_player": player,
                    "goal": 0,
                }
                played_matches = tournament.matches.filter(Q(command_a=command) | Q(command_b=command)).filter(status=True)
                for p_match in played_matches:
                    all_events = p_match.events.filter(event=Event.GOAL)
                    for m_event in all_events:
                        if player == m_event.scored:
                            scored_goal["goal"] = scored_goal.get("goal", 0) + 1

                scorers_table[player.last_name] = scored_goal

            for player in command.players.all():
                assistant_goal = {
                    "self_player": player,
                    "assist": 0,
                }
                played_matches = tournament.matches.filter(Q(command_a=command) | Q(command_b=command)).filter(status=True)
                for p_match in played_matches:
                    all_events = p_match.events.filter(event=Event.GOAL)
                    for m_event in all_events:
                        if player == m_event.assistant:
                            assistant_goal["assist"] = assistant_goal.get("assist", 0) + 1

                assistants_table[player.last_name] = assistant_goal

            tournament_table[command.name] = results

        if type == "table":
            return render(request, "templates/tournaments/table.html", context={
                'tournament_table': tournament_table,
            })

        elif type == "scorers":
            return render(request, "templates/tournaments/scorers.html", context={
                'scorers_table': scorers_table,
            })

        elif type == "assistants":
            return render(request, "templates/tournaments/assistant.html", context={
                'assistants_table': assistants_table,
            })

