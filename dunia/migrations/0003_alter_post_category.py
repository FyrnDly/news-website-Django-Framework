# Generated by Django 4.1.2 on 2022-11-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dunia', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('ekonomi', 'Ekonomi'), ('sosial-dan-budaya', 'Sosial Budaya'), ('pemerintahan', 'Pemerintah'), ('lainnya', 'Lainnya')], default='lainnya', max_length=255),
        ),
    ]
