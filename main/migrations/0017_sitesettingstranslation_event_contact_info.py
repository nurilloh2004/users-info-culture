# Generated by Django 2.2.7 on 2021-05-04 10:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_event_eventtranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettingstranslation',
            name='event_contact_info',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
