# Generated by Django 4.0.3 on 2022-03-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_submittedtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='submission',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]