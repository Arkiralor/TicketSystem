# Generated by Django 4.1.1 on 2022-09-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
