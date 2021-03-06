# Generated by Django 3.2.7 on 2022-01-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="email_is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="account",
            name="token",
            field=models.TextField(blank=True, null=True),
        ),
    ]
