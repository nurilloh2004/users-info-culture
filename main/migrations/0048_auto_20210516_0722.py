# Generated by Django 2.2.7 on 2021-05-16 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20210516_0718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={},
        ),
        migrations.AddField(
            model_name='media',
            name='view_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]