# Generated by Django 4.1 on 2022-08-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_dish_alter_stock_options_alter_stock_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='meal',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snack', 'Snack'), ('Dinner', 'Dinner')], default='Breakfast', max_length=10),
        ),
    ]
