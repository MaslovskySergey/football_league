# Generated by Django 4.0.2 on 2022-05-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0008_alter_player_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, upload_to='player/', verbose_name='Фото'),
        ),
    ]
