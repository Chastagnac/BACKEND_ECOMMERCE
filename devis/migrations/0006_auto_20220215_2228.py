# Generated by Django 3.2.10 on 2022-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0005_alter_devi_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devi',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Statu',
        ),
    ]