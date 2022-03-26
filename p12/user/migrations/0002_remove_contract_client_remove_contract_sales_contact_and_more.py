# Generated by Django 4.0.3 on 2022-03-19 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contract",
            name="client",
        ),
        migrations.RemoveField(
            model_name="contract",
            name="sales_contact",
        ),
        migrations.RemoveField(
            model_name="contract",
            name="support_contact",
        ),
        migrations.RemoveField(
            model_name="event",
            name="client",
        ),
        migrations.RemoveField(
            model_name="event",
            name="event_status",
        ),
        migrations.RemoveField(
            model_name="event",
            name="sales_contact",
        ),
        migrations.RemoveField(
            model_name="event",
            name="support_contact",
        ),
        migrations.DeleteModel(
            name="Client",
        ),
        migrations.DeleteModel(
            name="Contract",
        ),
        migrations.DeleteModel(
            name="Event",
        ),
        migrations.DeleteModel(
            name="EventStatu",
        ),
    ]
