# Generated by Django 3.0.8 on 2020-07-07 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_auto_20200707_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlalgorithmstatus',
            old_name='avtive',
            new_name='active',
        ),
    ]