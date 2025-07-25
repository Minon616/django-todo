# Generated by Django 5.2.3 on 2025-06-26 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tasks/')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todo_app.task')),
            ],
        ),
    ]
