# Generated by Django 4.1.5 on 2023-01-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDogadaTatil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='karavanlar',
            name='image',
            field=models.FileField(null=True, upload_to='', verbose_name='Model Resmi'),
        ),
    ]
