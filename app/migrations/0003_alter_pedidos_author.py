# Generated by Django 5.0.6 on 2024-12-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pedidos_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='author',
            field=models.CharField(help_text='Digite seu nominho', max_length=90, verbose_name='Autor'),
        ),
    ]