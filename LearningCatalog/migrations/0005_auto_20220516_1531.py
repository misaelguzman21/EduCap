# Generated by Django 3.2.12 on 2022-05-16 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearningCatalog', '0004_alter_archivo_orden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=900)),
                ('is_correct', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=900)),
                ('points', models.PositiveIntegerField()),
                ('answers', models.ManyToManyField(to='LearningCatalog.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quizzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('due', models.DateField(null=True)),
                ('allowed_attempts', models.PositiveIntegerField()),
                ('time_limit_mins', models.PositiveIntegerField()),
                ('questions', models.ManyToManyField(to='LearningCatalog.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attempter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField()),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.quizzes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.answer')),
                ('attempter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.attempter')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearningCatalog.quizzes')),
            ],
        ),
        migrations.AddField(
            model_name='leccion',
            name='quizzes',
            field=models.ManyToManyField(to='LearningCatalog.Quizzes'),
        ),
    ]
