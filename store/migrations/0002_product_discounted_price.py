# Generated by Django 5.0 on 2024-01-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
