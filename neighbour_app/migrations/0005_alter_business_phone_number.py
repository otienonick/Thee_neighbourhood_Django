# Generated by Django 3.2.8 on 2021-10-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour_app', '0004_business_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
