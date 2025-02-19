# Generated by Django 5.1.6 on 2025-02-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothes',
            options={'ordering': ['-id'], 'verbose_name': 'Одежда', 'verbose_name_plural': 'Одежда'},
        ),
        migrations.AlterModelOptions(
            name='clothingcategory',
            options={'ordering': ['name'], 'verbose_name': 'Категория одежды', 'verbose_name_plural': 'Категории одежды'},
        ),
        migrations.AlterField(
            model_name='clothes',
            name='clothing_category',
            field=models.ManyToManyField(related_name='clothes', to='clothes.clothingcategory'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='price',
            field=models.FloatField(default=300, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название одежды'),
        ),
        migrations.AlterField(
            model_name='clothingcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название категории'),
        ),
    ]
