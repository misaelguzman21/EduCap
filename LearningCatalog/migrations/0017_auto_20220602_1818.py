# Generated by Django 3.2.12 on 2022-06-02 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0016_auto_20220530_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leccion',
            name='liked',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
