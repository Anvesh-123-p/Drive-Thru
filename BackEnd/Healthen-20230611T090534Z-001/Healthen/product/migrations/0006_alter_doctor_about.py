# Generated by Django 4.0.2 on 2022-03-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_doctor_mobile_number_alter_user_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='about',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
