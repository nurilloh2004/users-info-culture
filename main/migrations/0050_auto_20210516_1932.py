# Generated by Django 2.2.7 on 2021-05-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_eventorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorder',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]