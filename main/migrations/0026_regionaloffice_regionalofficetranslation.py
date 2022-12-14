# Generated by Django 2.2.7 on 2021-05-12 10:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210512_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionalOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='/uploads/default/regional_office.png', upload_to='uploads/regional_office/')),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('name_in_english', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RegionalOfficeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('head_of_office', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main.RegionalOffice')),
            ],
            options={
                'verbose_name': 'regional office Translation',
                'db_table': 'main_regionaloffice_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
