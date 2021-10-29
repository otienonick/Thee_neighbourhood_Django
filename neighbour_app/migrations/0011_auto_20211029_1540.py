# Generated by Django 3.2.8 on 2021-10-29 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbour_app', '0010_auto_20211029_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
