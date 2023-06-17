# Generated by Django 4.2.1 on 2023-05-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('views', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
    ]