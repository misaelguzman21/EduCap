# Generated by Django 3.2.13 on 2022-06-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0027_auto_20220608_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuesta',
            name='id_leccion',
        ),
        migrations.AddField(
            model_name='encuesta',
            name='title_leccion',
            field=models.TextField(null=True),
        ),
    ]
