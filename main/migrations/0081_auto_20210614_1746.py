# Generated by Django 2.2.7 on 2021-06-14 12:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0080_album_albumimage_albumimagetranslation_albumtranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimagetranslation',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='albumtranslation',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albumtranslation',
            name='organizer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albumtranslation',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
