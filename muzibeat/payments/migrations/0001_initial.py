# Generated by Django 3.2.7 on 2021-09-19 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('price', models.CharField(max_length=40)),
                ('ref', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('d', 'Done'), ('f', 'Failed'), ('s', 'Suspended')], max_length=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
