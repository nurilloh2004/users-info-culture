# Generated by Django 2.2.7 on 2021-04-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210426_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfiletranslation',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
