# Generated by Django 4.2.2 on 2023-06-13 13:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("workLog", "0002_alter_worklog_borad_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="worklog",
            old_name="id",
            new_name="user_id",
        ),
    ]