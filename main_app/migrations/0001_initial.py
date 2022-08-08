# Generated by Django 4.1 on 2022-08-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('notable_ingredients', models.TextField(max_length=100)),
                ('scoville_scale', models.PositiveIntegerField()),
            ],
        ),
    ]
