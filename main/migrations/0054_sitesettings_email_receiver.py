# Generated by Django 2.2.7 on 2021-05-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_auto_20210516_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='email_receiver',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
