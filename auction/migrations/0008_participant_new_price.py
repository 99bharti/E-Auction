# Generated by Django 2.2.6 on 2020-06-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_aucted_product_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='new_price',
            field=models.IntegerField(null=True),
        ),
    ]
