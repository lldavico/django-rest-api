# Generated by Django 3.0.8 on 2020-07-13 02:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='email',
        ),
        migrations.AddField(
            model_name='article',
            name='discount',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.IntegerField(default=1000, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
