# Generated by Django 4.0 on 2022-01-10 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0003_alter_tweet_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
