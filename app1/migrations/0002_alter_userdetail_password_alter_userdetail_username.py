# Generated by Django 4.2.7 on 2024-01-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='Password',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='Username',
            field=models.TextField(),
        ),
    ]
