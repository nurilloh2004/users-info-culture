# Generated by Django 2.2.7 on 2021-05-27 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_keyindicator_keyindicatortranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpagedata',
            name='email3',
        ),
    ]
