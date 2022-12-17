# Generated by Django 2.2.7 on 2021-06-14 12:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0079_auto_20210609_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('fest', 'Festival'), ('competition', 'Competition')], max_length=255)),
                ('region', models.CharField(choices=[('local', 'Local'), ('international', 'International')], max_length=255)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/album/%Y/%m/%d')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Album')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AlbumTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('place', models.CharField(max_length=255)),
                ('organizer', ckeditor.fields.RichTextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.Album')),
            ],
            options={
                'verbose_name': 'Album Translation',
                'db_table': 'main_album_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AlbumImageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.AlbumImage')),
            ],
            options={
                'verbose_name': 'album image Translation',
                'db_table': 'main_albumimage_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]