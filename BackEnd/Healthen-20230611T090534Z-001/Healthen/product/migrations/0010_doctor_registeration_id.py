# Generated by Django 4.0.2 on 2022-03-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='registeration_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
