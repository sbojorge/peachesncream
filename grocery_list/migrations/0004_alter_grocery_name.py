# Generated by Django 3.2.20 on 2023-08-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_alter_grocery_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='name',
            field=models.CharField(default='My shopping list', max_length=500),
        ),
    ]