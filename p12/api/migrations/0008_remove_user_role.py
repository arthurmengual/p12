# Generated by Django 4.0.3 on 2022-03-17 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_eventstatus_eventstatu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]