# Generated by Django 3.2.11 on 2022-04-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_events', '0009_alter_reminders_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminders',
            name='event_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
