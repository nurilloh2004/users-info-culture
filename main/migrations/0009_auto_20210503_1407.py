# Generated by Django 2.2.7 on 2021-05-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210426_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannertranslation',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]
