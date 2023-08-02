# Generated by Django 3.2.20 on 2023-08-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0004_auto_20230802_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocery',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='grocery',
            name='quantity',
        ),
        migrations.AddField(
            model_name='grocery',
            name='shop',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
