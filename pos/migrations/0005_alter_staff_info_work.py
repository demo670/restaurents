# Generated by Django 4.2.6 on 2023-10-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_alter_staff_info_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_info',
            name='work',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
