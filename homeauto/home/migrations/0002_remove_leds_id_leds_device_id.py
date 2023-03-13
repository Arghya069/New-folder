# Generated by Django 4.1.5 on 2023-03-13 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="leds", name="id",),
        migrations.AddField(
            model_name="leds",
            name="device_id",
            field=models.TextField(
                default=django.utils.timezone.now,
                max_length=10,
                primary_key=True,
                serialize=False,
            ),
            preserve_default=False,
        ),
    ]
