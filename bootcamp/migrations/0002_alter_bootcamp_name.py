# Generated by Django 4.2.4 on 2023-09-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamp',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
