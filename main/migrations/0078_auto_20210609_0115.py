# Generated by Django 2.2.7 on 2021-06-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_auto_20210609_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posting_date',
            field=models.DateTimeField(null=True),
        ),
    ]
