# Generated by Django 3.2.10 on 2022-01-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0004_auto_20220112_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devi',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]