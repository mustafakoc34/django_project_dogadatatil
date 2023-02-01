# Generated by Django 4.1.5 on 2023-01-27 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDogadaTatil', '0013_alter_comment_karavan_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='bungalov_category',
            field=models.ManyToManyField(to='appDogadaTatil.bungalov', verbose_name='Bungalov Modelleri'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tent_category',
            field=models.ManyToManyField(to='appDogadaTatil.tent', verbose_name='Çadır Modelleri'),
        ),
    ]
