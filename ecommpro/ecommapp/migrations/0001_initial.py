# Generated by Django 5.0 on 2024-02-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('categories', models.CharField(choices=[('Electronic', 'electronic'), ('laptops', 'laptop'), ('shoes', 'shoes'), ('fashion', 'fashion')], max_length=250)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
