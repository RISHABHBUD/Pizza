# Generated by Django 3.0.5 on 2021-05-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzhut', '0013_delete_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='pizzaname', max_length=50)),
                ('shape1', models.CharField(blank=True, default='', max_length=50)),
                ('shape2', models.CharField(blank=True, default='', max_length=50)),
                ('size1', models.CharField(blank=True, default='', max_length=50)),
                ('size2', models.CharField(blank=True, default='', max_length=50)),
                ('size3', models.CharField(blank=True, default='', max_length=50)),
                ('size4', models.CharField(blank=True, default='', max_length=50)),
                ('size5', models.CharField(blank=True, default='', max_length=50)),
                ('size6', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
