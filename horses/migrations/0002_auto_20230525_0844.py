# Generated by Django 2.2.4 on 2023-05-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='age',
            field=models.CharField(default=None, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horse',
            name='description',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
