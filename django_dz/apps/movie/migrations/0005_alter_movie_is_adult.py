# Generated by Django 4.0.6 on 2022-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_is_adult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='is_adult',
            field=models.BooleanField(null=True, verbose_name='Is Adult'),
        ),
    ]
