# Generated by Django 5.0.2 on 2024-04-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0011_catagories'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='saleprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
