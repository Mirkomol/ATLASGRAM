# Generated by Django 3.2 on 2021-11-19 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtlasGramApp', '0002_postcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='author',
            new_name='user',
        ),
    ]