# Generated by Django 2.2.7 on 2021-05-17 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_remove_post_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationcategory',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
