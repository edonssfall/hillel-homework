# Generated by Django 4.0.6 on 2022-07-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(blank=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_year',
            field=models.DateField(blank=True, verbose_name='Birth Year'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_year',
            field=models.DateField(blank=True, verbose_name='Death Year'),
        ),
    ]