# Generated by Django 2.2.7 on 2021-05-27 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_organizationregion_organizationregiontranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.OrganizationRegion'),
        ),
    ]
