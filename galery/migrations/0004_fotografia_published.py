# Generated by Django 4.1.5 on 2023-01-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_alter_fotografia_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
