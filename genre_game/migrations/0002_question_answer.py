# Generated by Django 4.0 on 2021-12-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre_game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]