# Generated by Django 4.2.4 on 2023-08-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fretes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]