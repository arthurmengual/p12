# Generated by Django 4.0.3 on 2022-03-19 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("potential", "potential"), ("existing", "existing")],
                        default="potential",
                        max_length=10,
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=20)),
                ("compagny", models.CharField(max_length=50)),
                ("date_created", models.DateField(auto_now=True)),
                ("date_updated", models.DateField(auto_now=True)),
                (
                    "sales_contact",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"role": "sales"},
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="client_sales_contact",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "support_contact",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"role": "support"},
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="client_support_contact",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
