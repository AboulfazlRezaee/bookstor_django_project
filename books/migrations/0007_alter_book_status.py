# Generated by Django 4.2.7 on 2023-12-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_price_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('درخواست', 'Draft'), ('منتشر شده', 'Published')], max_length=10),
        ),
    ]
