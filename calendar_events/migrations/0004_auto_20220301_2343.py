# Generated by Django 3.2.11 on 2022-03-01 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_events', '0003_auto_20220228_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevents',
            name='timed',
        ),
        migrations.AlterField(
            model_name='calendarevents',
            name='end',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='calendarevents',
            name='start',
            field=models.CharField(max_length=255),
        ),
    ]
