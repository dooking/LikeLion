# Generated by Django 3.0.6 on 2020-05-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200516_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.TimeField(default='12:00:00'),
            preserve_default=False,
        ),
    ]
