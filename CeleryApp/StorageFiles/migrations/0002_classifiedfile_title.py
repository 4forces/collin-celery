# Generated by Django 3.1.5 on 2021-01-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StorageFiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classifiedfile',
            name='title',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
