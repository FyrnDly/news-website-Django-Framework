# Generated by Django 4.1.2 on 2022-11-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('category', models.CharField(choices=[('olahraga', 'Olahraga'), ('pola-hidup', 'Pola Hidup'), ('makanan', 'Makanan'), ('lainnya', 'Lainnya')], default='lainnya', max_length=255)),
                ('image', models.ImageField(upload_to='static/indonesia/')),
                ('body', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
