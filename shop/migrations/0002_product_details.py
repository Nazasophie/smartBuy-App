# Generated by Django 4.2.2 on 2023-06-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
