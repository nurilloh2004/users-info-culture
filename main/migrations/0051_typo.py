# Generated by Django 2.2.7 on 2021-05-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_auto_20210516_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
