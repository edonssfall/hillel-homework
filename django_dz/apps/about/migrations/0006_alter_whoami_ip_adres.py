# Generated by Django 4.0.6 on 2022-07-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_remove_whoami_ip_adress_whoami_ip_adres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whoami',
            name='ip_adres',
            field=models.CharField(max_length=16, null=True, verbose_name='IP'),
        ),
    ]
