# Generated by Django 3.2.9 on 2021-11-24 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211113_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_like',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='account.post_user'),
        ),
        migrations.CreateModel(
            name='User_Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('comment_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='account.post_comment')),
                ('post_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='account.post_user')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
