# Generated by Django 2.2 on 2022-12-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0086_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='json',
            name='name',
            field=models.CharField(max_length=50000),
        ),
    ]