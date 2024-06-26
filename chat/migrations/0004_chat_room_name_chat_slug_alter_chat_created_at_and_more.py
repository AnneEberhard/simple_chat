# Generated by Django 5.0.1 on 2024-06-04 07:31

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_message_chat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='room_name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_message_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
