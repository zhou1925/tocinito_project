# Generated by Django 3.2.7 on 2022-09-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
