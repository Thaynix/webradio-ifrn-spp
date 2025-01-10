# Generated by Django 5.0.6 on 2025-01-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_event_pedidos_status_alter_pedidos_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='color',
            field=models.CharField(choices=[('#005c81', 'azul'), ('#d40f60', 'rosa'), ('#f84339', 'laranja'), ('#e79a32', 'amarelo'), ('#368986', 'verde'), ('#7345d6', 'roxo'), ('#99b333', 'verde-claro')], default='#005c81', max_length=7),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='author',
            field=models.CharField(help_text='Digite seu nome', max_length=90, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='description',
            field=models.CharField(max_length=225, verbose_name='Nome da Música'),
        ),
    ]