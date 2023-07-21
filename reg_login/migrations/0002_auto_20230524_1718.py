# Generated by Django 2.2.4 on 2023-05-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=45)),
                ('pw', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
