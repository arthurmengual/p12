# Generated by Django 4.0.3 on 2022-03-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_eventstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('manager', 'manager'), ('sales', 'sales'), ('support', 'support')], default='else', max_length=20),
        ),
    ]