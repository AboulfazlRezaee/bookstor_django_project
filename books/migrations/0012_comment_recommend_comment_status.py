# Generated by Django 4.2.7 on 2023-12-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
