# Generated by Django 2.2.7 on 2021-05-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0071_organization_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyindicator',
            name='icon',
            field=models.CharField(help_text="Icons can be found from <a href='https://fontawesome.com/v5.15/icons'>here</a>", max_length=255),
        ),
    ]
