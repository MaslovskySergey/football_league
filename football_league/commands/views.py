from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CommandForm, PlayerForm
from .models import Command, Player


class CommandsView(View):
    def get(self, request, *args, **kwargs):
        commands = Command.objects.all()
        return render(request, 'templates/commands/commands.html', {'commands': commands})


class CreateCommandView(View):
    """
    # Return home page
    """

    def get(self, request, *args, **kwargs):
        form = CommandForm()
        data = {
            'form': form,
        }
        return render(request, "templates/commands/create.html", context=data)

    def post(self, request, *args, **kwargs):
        form = CommandForm(request.POST, request.FILES)
        if form.is_valid():
            command = form.save()
            # command = form.cleaned_data.get("commands").pk
            return redirect('create_capitan', command.pk)


class InfoCommandView(View):

    def get(self, request, id, *args, **kwargs):

        command = get_object_or_404(Command, id=id)
        data = {"command": command, }
        if request.user.is_superuser or request.user.is_authenticated and request.user.player.command == command:
            data["form"] = PlayerForm(initial={"command": command})
        return render(request, "templates/commands/info_command.html", context=data)

    def post(self, request, *args, **kwargs):

        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get("command").pk
            return redirect('id', id)


class CreateCapitanView(View):

    def get(self, request, id, *args, **kwargs):

        command = get_object_or_404(Command, pk=id)
        form = PlayerForm(initial={"command": command})

        return render(request, "templates/commands/create_capitan.html", context={
            "command": command,
            "form": form,
        })

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PlayerForm(request.POST, request.FILES)
            if form.is_valid():
                # capitan = Player(**form.cleaned_data, is_captain=True).save()
                capitan = form.save(commit=True)
                capitan.is_captain = True
                capitan.user = request.user
                capitan.save()
                id = form.cleaned_data.get("command").pk
                return redirect('id', id)


class InfoPlayerView(View):

    def get(self, request, id, *args, **kwargs):

        player = get_object_or_404(Player, id=id)
        return render(request, "templates/commands/player.html", context={
            "player": player,
        })