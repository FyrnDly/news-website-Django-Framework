# Generated by Django 4.1.2 on 2022-11-11 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indonesia', '0004_post_penulis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='penulis',
            new_name='author',
        ),
    ]
