# Generated by Django 4.0.3 on 2022-03-16 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_event_support_client_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'sales'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_sales_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='support_contact',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'support'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_support_contact', to=settings.AUTH_USER_MODEL),
        ),
    ]