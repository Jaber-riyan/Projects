# Generated by Django 4.2.7 on 2023-12-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bankrupt',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
