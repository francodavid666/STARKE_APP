# Generated by Django 4.1 on 2022-12-06 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('STARKE_APP', '0002_remove_model2_model1_ptr_remove_model34_model1_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagos_model',
            name='id',
        ),
        migrations.AddField(
            model_name='pagos_model',
            name='fichatec_model_ptr',
            field=models.OneToOneField(auto_created=True, default=2, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='STARKE_APP.fichatec_model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagos_model',
            name='dias_de_entrenamiento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pagos_model',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pagos_model',
            name='fecha_vencimiento',
            field=models.DateField(null=True),
        ),
    ]