# Generated by Django 3.2.9 on 2021-12-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0008_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='playlist',
            new_name='song',
        ),
    ]