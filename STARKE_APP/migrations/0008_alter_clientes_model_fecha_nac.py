# Generated by Django 4.1 on 2022-11-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STARKE_APP', '0007_alter_clientes_model_fecha_nac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes_model',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True),
        ),
    ]
