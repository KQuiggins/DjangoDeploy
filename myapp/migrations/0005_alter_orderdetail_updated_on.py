# Generated by Django 4.0 on 2023-03-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
