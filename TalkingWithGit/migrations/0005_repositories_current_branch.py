# Generated by Django 5.0.1 on 2024-02-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TalkingWithGit', '0004_alter_repositories_directory'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositories',
            name='current_branch',
            field=models.CharField(default='main', max_length=250),
        ),
    ]
