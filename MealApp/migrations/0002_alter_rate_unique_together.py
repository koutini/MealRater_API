# Generated by Django 3.2.7 on 2021-12-09 14:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MealApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('user', 'meal')},
        ),
    ]
