# Generated by Django 4.0.3 on 2022-04-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='players',
            options={'verbose_name': 'Игрок', 'verbose_name_plural': 'Игроки'},
        ),
        migrations.AlterField(
            model_name='players',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Фамилия имя'),
        ),
    ]