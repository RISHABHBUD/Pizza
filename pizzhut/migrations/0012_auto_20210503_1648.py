# Generated by Django 3.0.5 on 2021-05-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0011_pizza_shape1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
