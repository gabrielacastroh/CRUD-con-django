# Generated by Django 4.0.3 on 2022-08-18 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
        ('asignaturas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='id_profesor',
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesores.profesor'),
        ),
    ]
