# Generated by Django 4.1 on 2022-10-31 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STARKE_APP', '0003_clientes_model_delete_persona_delete_persona_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes_model',
            name='mail',
        ),
    ]