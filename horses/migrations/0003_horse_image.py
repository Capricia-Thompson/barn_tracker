# Generated by Django 2.2.4 on 2023-05-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0002_auto_20230525_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='image',
            field=models.ImageField(default=None, upload_to='horse_pics/'),
            preserve_default=False,
        ),
    ]