# Generated by Django 5.2.1 on 2025-06-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_alter_diplomaticterm_related_countries_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['publication_date']},
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
