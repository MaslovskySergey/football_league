# Generated by Django 4.0.2 on 2022-05-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0007_alter_command_command_photo_alter_command_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(default='static/img/player.jpg', upload_to='player/', verbose_name='Фото'),
        ),
    ]