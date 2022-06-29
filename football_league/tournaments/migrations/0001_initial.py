# Generated by Django 4.0.3 on 2022-04-30 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commands', '0003_alter_command_name_alter_player_is_captain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField(verbose_name='Дата начала турнира')),
                ('commands', models.ManyToManyField(to='commands.command')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('command_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='commands.command')),
                ('command_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='commands.command')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='tournaments.tournament')),
            ],
            options={
                'ordering': ['-date_and_time'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.IntegerField()),
                ('event', models.CharField(choices=[('Гол', 'Гол'), ('Карточка', 'Карточка')], max_length=50, verbose_name='Событие')),
                ('color_card', models.CharField(blank=True, choices=[('Красная', 'Красная'), ('Желтая', 'Желтая')], max_length=50, verbose_name='Карточка')),
                ('assistant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assists', to='commands.player')),
                ('get_a_card', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='commands.player')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='tournaments.match')),
                ('scored', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='commands.player')),
            ],
        ),
    ]