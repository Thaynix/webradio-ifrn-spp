# Generated by Django 5.0.1 on 2024-03-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webradio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Imagem'),
        ),
    ]
