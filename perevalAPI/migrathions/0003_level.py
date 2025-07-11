# Generated by Django 5.1 on 2024-10-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevalAPI', '0002_coordinates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spring', models.CharField(choices=[('II', 'Категория II'), ('V', 'Категория V'), ('VI', 'Категория VI'), ('III', 'Категория III'), ('I', 'Категория I'), ('IV', 'Категория IV')], default='I', max_length=3, verbose_name='Весна')),
                ('summer', models.CharField(choices=[('II', 'Категория II'), ('V', 'Категория V'), ('VI', 'Категория VI'), ('III', 'Категория III'), ('I', 'Категория I'), ('IV', 'Категория IV')], default='I', max_length=3, verbose_name='Лето')),
                ('autumn', models.CharField(choices=[('II', 'Категория II'), ('V', 'Категория V'), ('VI', 'Категория VI'), ('III', 'Категория III'), ('I', 'Категория I'), ('IV', 'Категория IV')], default='I', max_length=3, verbose_name='Осень')),
                ('winter', models.CharField(choices=[('II', 'Категория II'), ('V', 'Категория V'), ('VI', 'Категория VI'), ('III', 'Категория III'), ('I', 'Категория I'), ('IV', 'Категория IV')], default='I', max_length=3, verbose_name='Зима')),
            ],
        ),
    ]