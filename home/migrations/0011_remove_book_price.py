# Generated by Django 3.0.2 on 2021-04-25 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210425_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]