# Generated by Django 5.0.1 on 2024-02-28 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruit',
            name='sun',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='sun',
        ),
        migrations.RemoveField(
            model_name='vegetable',
            name='sun',
        ),
    ]
