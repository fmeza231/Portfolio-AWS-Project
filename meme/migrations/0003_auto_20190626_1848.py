# Generated by Django 2.2.2 on 2019-06-26 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0002_auto_20190626_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='orig_url',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='s3_url',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='text',
        ),
    ]