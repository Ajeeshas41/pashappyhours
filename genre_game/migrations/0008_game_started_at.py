# Generated by Django 4.0 on 2021-12-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre_game', '0007_genreteam_questions_answered_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]