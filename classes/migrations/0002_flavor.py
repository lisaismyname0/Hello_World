# Generated by Django 4.0.5 on 2022-06-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flavor_description', models.CharField(blank=True, max_length=150, null=True)),
                ('local', models.BooleanField(null=True)),
            ],
        ),
    ]
