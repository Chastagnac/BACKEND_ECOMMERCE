# Generated by Django 3.2.10 on 2022-01-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0003_auto_20220112_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devi',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='devi',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]