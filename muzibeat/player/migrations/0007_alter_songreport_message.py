# Generated by Django 3.2.9 on 2021-12-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_songreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songreport',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
