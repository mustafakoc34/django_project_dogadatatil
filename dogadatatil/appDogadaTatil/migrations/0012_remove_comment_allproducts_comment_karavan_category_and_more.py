# Generated by Django 4.1.5 on 2023-01-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDogadaTatil', '0011_remove_comment_category_allproducts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='allproducts',
        ),
        migrations.AddField(
            model_name='comment',
            name='karavan_category',
            field=models.ManyToManyField(to='appDogadaTatil.karavanlar', verbose_name=''),
        ),
        migrations.DeleteModel(
            name='AllProducts',
        ),
    ]
