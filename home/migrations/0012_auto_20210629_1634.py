# Generated by Django 3.1.7 on 2021-06-29 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='email',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='donate',
            name='adderess',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='donate',
            name='message',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='donate',
            name='name',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='donate',
            name='service',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
