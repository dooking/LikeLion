# Generated by Django 3.0.6 on 2020-05-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolist',
            name='dday',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]