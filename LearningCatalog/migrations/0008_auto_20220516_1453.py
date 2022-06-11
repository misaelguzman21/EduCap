# Generated by Django 3.2.13 on 2022-05-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0007_auto_20220516_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta1', models.IntegerField()),
                ('pregunta2', models.IntegerField()),
                ('pregunta3', models.IntegerField()),
                ('pregunta4', models.IntegerField()),
                ('pregunta5', models.IntegerField()),
                ('opinion', models.TextField(max_length=500, verbose_name='Opinion')),
            ],
        ),
        migrations.CreateModel(
            name='Leccion_Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='ejercicio',
            name='imagen',
        ),
        migrations.DeleteModel(
            name='Estudiante_Encuesta_Leccion',
        ),
        migrations.AddField(
            model_name='leccion_ejercicio',
            name='ejercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.ejercicio'),
        ),
        migrations.AddField(
            model_name='leccion_ejercicio',
            name='leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.leccion'),
        ),
    ]
