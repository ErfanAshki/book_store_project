# Generated by Django 5.1.3 on 2024-11-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='covers',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers'),
        ),
    ]
