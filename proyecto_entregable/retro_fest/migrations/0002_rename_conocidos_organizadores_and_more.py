# Generated by Django 4.0.4 on 2022-06-05 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retro_fest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conocidos',
            new_name='Organizadores',
        ),
        migrations.RenameModel(
            old_name='Familia',
            new_name='Punto_de_venta',
        ),
        migrations.RenameField(
            model_name='amigos',
            old_name='amigo_de',
            new_name='puesto',
        ),
        migrations.RenameField(
            model_name='organizadores',
            old_name='conocido_de',
            new_name='Puesto',
        ),
        migrations.RenameField(
            model_name='punto_de_venta',
            old_name='parentezco',
            new_name='puesto',
        ),
    ]
