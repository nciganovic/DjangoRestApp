# Generated by Django 2.2.6 on 2019-11-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191030_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amazon_link',
            field=models.CharField(default='', max_length=500),
        ),
    ]