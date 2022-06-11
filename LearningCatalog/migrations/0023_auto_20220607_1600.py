# Generated by Django 3.2.13 on 2022-06-07 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearningCatalog', '0022_auto_20220607_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerexercise',
            old_name='answer_text_exercise',
            new_name='answer_text',
        ),
        migrations.RenameField(
            model_name='answerexercise',
            old_name='is_correct_exercise',
            new_name='is_correct',
        ),
        migrations.RenameField(
            model_name='attempterexercise',
            old_name='completed_exercise',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='attempterexercise',
            old_name='score_exercise',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='date_exercise',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='description_exercise',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='due_exercise',
            new_name='due',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='questions_exercise',
            new_name='questions',
        ),
        migrations.RenameField(
            model_name='exercises',
            old_name='title_exercise',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='questionexercise',
            old_name='answers_exercise',
            new_name='answers',
        ),
        migrations.RenameField(
            model_name='questionexercise',
            old_name='points_exercise',
            new_name='points',
        ),
        migrations.RenameField(
            model_name='questionexercise',
            old_name='question_text_exercise',
            new_name='question_text',
        ),
    ]
