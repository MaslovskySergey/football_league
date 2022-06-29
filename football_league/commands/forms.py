from django.forms import ModelForm, TextInput
from .models import Command, Player
from django import forms


class CommandForm(ModelForm):
    class Meta:
        model = Command
        fields = ['name', 'logo', 'command_photo']

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Введите название команды",

            })
        }


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'date_of_birth', 'role', 'is_captain', 'command', 'photo']

        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя",
                "required": "required",
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Фамилия",
            }),
            'role': forms.Select(),
            "command": forms.Select(choices=()),
        }