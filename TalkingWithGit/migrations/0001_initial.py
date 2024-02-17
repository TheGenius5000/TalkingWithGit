# Generated by Django 5.0.1 on 2024-01-22 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('unique_name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('directory', models.CharField(default='D:/GitLab/gxb199/git_repositories', editable=False, max_length=250)),
                ('collaborators', models.ManyToManyField(related_name='repositories_collaborators', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repositories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]