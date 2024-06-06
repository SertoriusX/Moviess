# Generated by Django 5.0.3 on 2024-06-04 19:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_admin', '0002_adminlastmovies'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMovies',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('nota', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ManyToManyField(blank=True, to='is_admin.category')),
            ],
        ),
    ]
