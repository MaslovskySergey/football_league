# Generated by Django 4.0.3 on 2022-04-30 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0003_alter_command_name_alter_player_is_captain_and_more'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='get_a_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='commands.player'),
        ),
    ]
