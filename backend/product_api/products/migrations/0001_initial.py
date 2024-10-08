# Generated by Django 5.0 on 2024-09-19 06:52

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
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
