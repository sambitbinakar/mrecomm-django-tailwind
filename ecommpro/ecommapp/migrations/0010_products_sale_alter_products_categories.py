# Generated by Django 5.0.2 on 2024-04-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0009_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='categories',
            field=models.CharField(choices=[('Electronic', 'electronic'), ('Fashion', 'Fashion'), ('Grocery', 'Grocery'), ('Home & Furniture', 'Home & furniture'), ('Mobiles', 'mobiles'), ('Appliances', 'Appliance'), ('watches', 'watches')], max_length=250),
        ),
    ]
