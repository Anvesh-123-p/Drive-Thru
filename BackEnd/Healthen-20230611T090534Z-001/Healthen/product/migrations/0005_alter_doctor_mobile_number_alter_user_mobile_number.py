# Generated by Django 4.0.2 on 2022-03-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_doctor_profile_user_profile_alter_doctor_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.BigIntegerField(),
        ),
    ]
