# Generated by Django 3.1 on 2020-09-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
    ]