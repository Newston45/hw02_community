# Generated by Django 2.2.19 on 2023-01-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230130_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
