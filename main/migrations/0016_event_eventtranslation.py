# Generated by Django 2.2.7 on 2021-05-04 08:24

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210503_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='defaults/event.png', upload_to='uploads/event/%Y/%m/%d')),
                ('event_type', models.CharField(choices=[('event', 'Event'), ('exhibition', 'Exhibition')], max_length=255)),
                ('providing_date', models.DateField()),
                ('price', models.IntegerField()),
                ('location', geoposition.fields.GeopositionField(max_length=42, null=True)),
            ],
            options={
                'ordering': ['providing_date'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('note', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.Event')),
            ],
            options={
                'verbose_name': 'event Translation',
                'db_table': 'main_event_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
