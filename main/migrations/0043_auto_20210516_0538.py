# Generated by Django 2.2.7 on 2021-05-16 00:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20210515_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mediaobject',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/media/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'aac'])]),
        ),
    ]