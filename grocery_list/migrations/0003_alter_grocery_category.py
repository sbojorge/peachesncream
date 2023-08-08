# Generated by Django 3.2.20 on 2023-08-08 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_alter_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='category',
            field=models.CharField(choices=[('groceries', 'Groceries'), ('school', 'School'), ('hardware', 'Hardware'), ('travel', 'Travel'), ('gifts', 'Gifts'), ('decoration', 'Decoration'), ('lifestyle', 'Lifestyle'), ('wishlist', 'Wishlist'), ('none', "I don't want a category")], default='groceries', max_length=20),
        ),
    ]