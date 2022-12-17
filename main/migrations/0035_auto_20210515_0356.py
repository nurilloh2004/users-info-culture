# Generated by Django 2.2.7 on 2021-05-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210515_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='statistics_accepted',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='statistics_not_solved',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='statistics_on_process',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='statistics_solved',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
