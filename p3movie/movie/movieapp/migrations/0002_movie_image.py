# Generated by Django 3.2.16 on 2022-12-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='dfghjkl', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
