# Generated by Django 3.2.20 on 2023-08-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0005_auto_20230802_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='category',
            field=models.CharField(choices=[('groceries', 'Groceries'), ('school', 'School'), ('hardware', 'Hardware'), ('travel', 'Travel'), ('gifts', 'Gifts'), ('decoration', 'Decoration'), ('lifestyle', 'Lifestyle'), ('wishlist', 'Wishlist')], default=' ', max_length=20),
            preserve_default=False,
        ),
    ]