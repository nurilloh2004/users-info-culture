# Generated by Django 2.2.7 on 2021-06-08 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0076_auto_20210609_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='posting_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
