# Generated by Django 4.1.5 on 2023-02-01 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appDogadaTatil', '0018_alter_karavanlar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bungalov',
            options={'verbose_name_plural': 'Bungalov'},
        ),
        migrations.AlterModelOptions(
            name='karavanlar',
            options={'verbose_name_plural': 'Karavan'},
        ),
        migrations.AlterModelOptions(
            name='tent',
            options={'verbose_name_plural': 'Çadır'},
        ),
        migrations.RenameField(
            model_name='bungalov',
            old_name='aciklama',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='bungalov',
            old_name='bungalovModeli',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='karavanlar',
            old_name='aciklama',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='karavanlar',
            old_name='karavanModeli',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tent',
            old_name='aciklama',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tent',
            old_name='cadirModeli',
            new_name='title',
        ),
    ]
