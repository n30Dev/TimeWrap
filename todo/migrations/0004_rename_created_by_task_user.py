# Generated by Django 4.2 on 2023-05-05 20:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0003_rename_user_task_created_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="created_by",
            new_name="user",
        ),
    ]
