# Generated by Django 5.0 on 2024-03-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0002_alter_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cata_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]