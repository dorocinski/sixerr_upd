# Generated by Django 3.0.4 on 2020-04-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(max_length=500),
        ),
    ]