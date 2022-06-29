# Generated by Django 4.0.3 on 2022-05-02 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0003_alter_command_name_alter_player_is_captain_and_more'),
        ('tournaments', '0002_alter_event_get_a_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='event',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='tournaments.match'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='commands',
            field=models.ManyToManyField(related_name='tournaments', to='commands.command'),
        ),
    ]
