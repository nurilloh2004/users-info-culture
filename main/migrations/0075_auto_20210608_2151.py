# Generated by Django 2.2.7 on 2021-06-08 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0074_auto_20210608_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['posting_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
