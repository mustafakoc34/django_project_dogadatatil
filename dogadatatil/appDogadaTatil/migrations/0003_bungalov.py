# Generated by Django 4.1.5 on 2023-01-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDogadaTatil', '0002_karavanlar_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bungalov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bungalovModeli', models.CharField(max_length=200, verbose_name='Bungalov Modeli')),
                ('aciklama', models.TextField(max_length=200, verbose_name='Karavan Detayı')),
                ('image', models.FileField(null=True, upload_to='', verbose_name='Model Resmi')),
            ],
        ),
    ]
