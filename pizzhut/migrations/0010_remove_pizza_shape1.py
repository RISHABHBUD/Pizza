# Generated by Django 3.0.5 on 2021-05-03 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0009_auto_20210503_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='shape1',
        ),
    ]
