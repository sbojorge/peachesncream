# Generated by Django 3.2.20 on 2023-08-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0006_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='category',
            field=models.CharField(choices=[('groceries', 'Groceries'), ('school', 'School'), ('hardware', 'Hardware'), ('travel', 'Travel'), ('gifts', 'Gifts'), ('decoration', 'Decoration'), ('lifestyle', 'Lifestyle'), ('wishlist', 'Wishlist')], default='Shopping', max_length=20),
        ),
    ]