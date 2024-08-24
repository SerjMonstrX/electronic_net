# Generated by Django 5.1 on 2024-08-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название продукта')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='модель продукта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание продукта')),
                ('release_date', models.DateField(verbose_name='дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
