# Generated by Django 5.0.6 on 2024-12-09 20:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_solicitationmusic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SolicitationMusic',
            new_name='Pedidos',
        ),
    ]
