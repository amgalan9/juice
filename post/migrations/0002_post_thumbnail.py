# Generated by Django 3.1.1 on 2020-09-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnails'),
        ),
    ]
