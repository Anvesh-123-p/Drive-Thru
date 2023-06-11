# Generated by Django 4.0.2 on 2022-03-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_doctor_email_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('OH', 'On Hold'), ('SH', 'Scheduled'), ('RJ', 'Rejected')], default='OH', max_length=2),
        ),
    ]