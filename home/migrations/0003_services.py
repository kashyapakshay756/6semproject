# Generated by Django 3.1.7 on 2021-06-16 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210417_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('services', models.CharField(max_length=50)),
                ('adderess', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]
