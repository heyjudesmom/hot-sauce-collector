# Generated by Django 4.1 on 2022-08-09 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.CharField(choices=[('F', 'Full'), ('H', 'Half'), ('L', 'Low'), ('E', 'Empty')], default='F', max_length=1)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.sauce')),
            ],
        ),
    ]
