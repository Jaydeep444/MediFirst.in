# Generated by Django 3.1.3 on 2020-11-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfinal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
