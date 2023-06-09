# Generated by Django 3.2.18 on 2023-04-27 23:00

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_auto_20230427_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='item',
            field=djrichtextfield.models.RichTextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='name',
            field=models.CharField(default='My grocery list', max_length=500),
        ),
    ]
