# Generated by Django 4.0.2 on 2022-03-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_remove_task_user_id_task_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]