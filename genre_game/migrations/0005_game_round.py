# Generated by Django 4.0 on 2021-12-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre_game', '0004_game_is_locked_game_won_genreteam_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.IntegerField(default=0),
        ),
    ]